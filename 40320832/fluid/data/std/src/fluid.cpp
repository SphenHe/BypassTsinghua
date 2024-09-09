#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <array>
#include <memory>

#include <Eigen/Dense>
#include <Eigen/Sparse>
#include <Eigen/SparseCholesky>
#include <rapidjson/document.h>
#include <gif.h>
#include <H5Cpp.h>

// #define AUX_HDF_OUTPUT
#define ENABLE_GIF

using namespace Eigen;
using namespace H5;
using namespace std;

typedef SimplicialLDLT<SparseMatrix<double, RowMajor>> Solver;

template<typename Mat>
inline
void copy_to_boundary(Mat &field, double factor) {
  field.topRows(1) = field.topRows(2).bottomRows(1) * factor;
  field.bottomRows(1) = field.bottomRows(2).topRows(1) * factor;
  field.leftCols(1) = field.leftCols(2).rightCols(1) * factor;
  field.rightCols(1) = field.rightCols(2).leftCols(1) * factor;
}

template<typename Mat>
inline
std::array<MatrixXd, 2> gradient(const Mat &field) {
  const size_t rows = field.rows();
  const size_t cols = field.cols();

  std::array<MatrixXd, 2> result = {MatrixXd{rows, cols}, MatrixXd{rows, cols}};

  result[0].block(1, 0, rows-2, cols) = (field.bottomRows(rows-2) - field.topRows(rows-2)) / 2;
  result[1].block(0, 1, rows, cols-2) = (field.rightCols(cols-2) - field.leftCols(rows-2)) / 2;

  return result;
}

template<typename Mat>
inline
MatrixXd divergence(const Mat (&field)[2]) {
  const size_t rows = field[0].rows();
  const size_t cols = field[0].cols();

  MatrixXd result{rows, cols};

  result.block(1, 0, rows-2, cols) = (field[0].bottomRows(rows-2) - field[0].topRows(rows-2)) / 2;
  result.block(0, 1, rows, cols-2) += (field[1].rightCols(cols-2) - field[1].leftCols(rows-2)) / 2;

  return result;
}

inline
double access(const MatrixXd &field, ssize_t x, ssize_t y) {
  if(x < 0) x = 0;
  else if(x >= field.rows()) x = field.rows() - 1;

  if(y < 0) y = 0;
  else if(y >= field.cols()) y = field.cols() - 1;

  return field(x, y);
}

inline size_t colmajor_idx(size_t height, size_t width, size_t i, size_t j) {
  (void) width;
  return j * height + i;
}

inline bool in_boundary(size_t height, size_t width, size_t i, size_t j) {
  return i == 0 || i == height - 1 || j == 0 || j == width - 1;
}

const pair<ssize_t, ssize_t> LAPLACIAN_IDX[4] = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};

// Solve (rI + s\nabla^2)x = b
template<typename S>
void construct_poisson_solver(S &solver, size_t height, size_t width, double r, double s, double refl) {
  SparseMatrix<double, RowMajor> A(height * width, height * width);
  for(size_t j = 0; j < width; ++j)
    for(size_t i = 0; i < height; ++i) {
      size_t self_idx = colmajor_idx(height, width, i, j);

      if(in_boundary(height, width, i, j)) {
        A.insert(self_idx, self_idx) = 1;
        continue;
      }

      double base = r - 4 * s;

      for(const auto &[di, dj] : LAPLACIAN_IDX) {
        const size_t ni = i + di;
        const size_t nj = j + dj;
        if(in_boundary(height, width, ni, nj)) base += refl * s;
        else A.insert(self_idx, colmajor_idx(height, width, ni, nj)) = s;
      }

      A.insert(self_idx, self_idx) = base;
    }

  solver.compute(A);

  if(solver.info() != Success) {
    cout<<"Poisson solver construction failed"<<endl;
    std::exit(1);
  }
}

inline
double bilinear_interp(const MatrixXd &field, double x, double y) {
  ssize_t xr = floor(x);
  ssize_t yr = floor(y);

  double dx = x - xr;
  double dy = y - yr;

  double tl = access(field, xr, yr);
  double tr = access(field, xr, yr + 1);
  double bl = access(field, xr + 1, yr);
  double br = access(field, xr + 1, yr + 1);

  double l = tl * (1 - dx) + bl * dx;
  double r = tr * (1 - dx) + br * dx;

  return l * (1 - dy) + r * dy;
}

template<size_t STACK>
void write_dataset(DataSet &ds, const MatrixXd mat[STACK]) {
  size_t height = mat[0].rows();
  size_t width = mat[0].cols();

  unique_ptr<double[]> buffer(new double[height * width * STACK]);
  for(size_t i = 0; i < height; ++i)
    for(size_t j = 0; j < width; ++j)
      for(size_t s = 0; s < STACK; ++s)
        buffer[s + (j + i * width) * STACK] = mat[s](i, j);

  ds.write(buffer.get(), PredType::NATIVE_DOUBLE);
}

class Simulator {
  public:
    Simulator(size_t h, size_t w, double viscosity) :
      height(h),
      width(w),
      dyes{{h, w}, {h, w}, {h, w}},
      velocity{{h, w}, {h, w}}
    {
      construct_poisson_solver(diffusion_solver, h, w, 1, -viscosity, -1);
      construct_poisson_solver(pressure_solver, h, w, 0, 1, 1);
    }

    void splat(
      pair<double, double> center,
      double radius,
      pair<double, double> accel,
      array<double, 3> inj
    ) {
      for(ssize_t j = floor(center.second - radius) - 1; j < ceil(center.second + radius) + 1; ++j)
        for(ssize_t i = floor(center.first - radius) - 1; i < ceil(center.first + radius) + 1; ++i) {
          if(i < 0 || i >= (ssize_t) height || j < 0 || j >= (ssize_t) width) continue;

          const double dx = i - center.first;
          const double dy = j - center.second;
          if(dx * dx + dy * dy > radius * radius) continue;

          velocity[0](i, j) += accel.first;
          velocity[1](i, j) += accel.second;

          for(size_t d = 0; d < 3; ++d) dyes[d](i, j) = min(inj[d] + dyes[d](i, j), 1.0);
        }
    }

    void step(size_t t) {

#ifdef AUX_HDF_OUTPUT
      string name = string("aux/") + to_string(t) + ".before.hdf5";
      output_hdf(name.c_str());
#else
      (void) t;
#endif

      // Advection
      // cout<<"Advection..."<<endl;
      MatrixXd advected_velocity[2] = {{height, width}, {height, width}};
      MatrixXd advected_dyes[3] = {{height, width}, {height, width}, {height, width}};
      for(size_t j = 0; j < width; ++j)
        for(size_t i = 0; i < height; ++i) {
          double orig_x = i - velocity[0](i, j);
          double orig_y = j - velocity[1](i, j);

          for(int dim = 0; dim < 2; ++dim)
            advected_velocity[dim](i, j) = bilinear_interp(velocity[dim], orig_x, orig_y);

          for(int dye = 0; dye < 3; ++dye)
            advected_dyes[dye](i, j) = bilinear_interp(dyes[dye], orig_x, orig_y);
        }

      for(int dim = 0; dim < 3; ++dim) {
        copy_to_boundary(advected_dyes[dim], 0); // Set dye outside of boundary to zero
        dyes[dim] = advected_dyes[dim];
      }

      for(int dim = 0; dim < 2; ++dim) copy_to_boundary(advected_velocity[dim], -1);

#ifdef AUX_HDF_OUTPUT
      for(int dim = 0; dim < 2; ++dim) velocity[dim] = advected_velocity[dim];
      name = string("aux/") + to_string(t) + ".advection.hdf5";
      output_hdf(name.c_str());
#endif

      // Diffusion
      // cout<<"Diffusion..."<<endl;
      Map<VectorXd> velocity_views[2]{
        {advected_velocity[0].data(), advected_velocity[0].size()},
        {advected_velocity[1].data(), advected_velocity[1].size()}
      };

      VectorXd diffused_velocity_pre[2]{
        diffusion_solver.solve(velocity_views[0]),
        diffusion_solver.solve(velocity_views[1]),
      };

      Map<MatrixXd> diffused_velocity[2]{
        {diffused_velocity_pre[0].data(), (ssize_t) height, (ssize_t) width},
        {diffused_velocity_pre[1].data(), (ssize_t) height, (ssize_t) width}
      };

      for(int dim = 0; dim < 2; ++dim) copy_to_boundary(diffused_velocity[dim], -1);

#ifdef AUX_HDF_OUTPUT
      for(int dim = 0; dim < 2; ++dim) velocity[dim] = diffused_velocity[dim];
      name = string("aux/") + to_string(t) + ".diffusion.hdf5";
      output_hdf(name.c_str());
#endif
      
      // Projection
      // cout<<"Projection..."<<endl;
      MatrixXd div = divergence<Map<MatrixXd>>(diffused_velocity);
      Map<VectorXd> div_view(div.data(), div.size());
      VectorXd pressure_pre = pressure_solver.solve(div_view);
      Map<MatrixXd> pressure(pressure_pre.data(), height, width);
      copy_to_boundary(pressure, 1);
      auto grad = gradient(pressure);

      for(int dim = 0; dim < 2; ++dim)
        velocity[dim] = diffused_velocity[dim] - grad[dim];

      for(int dim = 0; dim < 2; ++dim) copy_to_boundary(velocity[dim], -1);

#ifdef AUX_HDF_OUTPUT
      name = string("aux/") + to_string(t) + ".projection.hdf5";
      output_hdf(name.c_str());
#endif
    }

    void write_frame(unique_ptr<uint8_t[]> &buffer) const {
      for(size_t i = 0; i < height; ++i)
        for(size_t j = 0; j < width; ++j) {
          for(size_t dim = 0; dim < 3; ++dim)
            buffer[(i * width + j)*4 + dim] = (uint8_t) round(255.0 * dyes[dim](i, j));
          buffer[(i * width + j)*4 + 3] = 255;
        }
    }

    void write_dyes(DataSet &ds) const {
      write_dataset<3>(ds, dyes);
    }

    void write_velocity(DataSet &ds) const {
      write_dataset<2>(ds, velocity);
    }

    void output_hdf(const char *dest) {
      H5File hdf5(dest, H5F_ACC_TRUNC);
      hsize_t velocity_dim[] = { height, width, 2 };
      hsize_t dyes_dim[] = { height, width, 3 };

      DataSpace velocity_space(3, velocity_dim);
      DataSpace dyes_space(3, dyes_dim);

      FloatType hdf_type(PredType::NATIVE_DOUBLE);
      hdf_type.setOrder(H5T_ORDER_LE);

      DataSet velocity_set = hdf5.createDataSet("velocity", PredType::NATIVE_DOUBLE, velocity_space);
      DataSet dyes_set = hdf5.createDataSet("dyes", PredType::NATIVE_DOUBLE, dyes_space);

      write_velocity(velocity_set);
      write_dyes(dyes_set);
    }

  private:
    size_t height, width;
    MatrixXd dyes[3];
    MatrixXd velocity[2];
    Solver diffusion_solver, pressure_solver;
};

typedef struct {
  size_t t_from, t_to;
  pair<double, double> c;
  pair<double, double> a;
  double r;
  array<double, 3> d;
} Splat; 

int main(int argc, char **argv) {
#ifdef ENABLE_GIF
  if(argc != 4) {
    cout<<"Usage: fluid_sim <input> <hdf_output> <gif_output>";
    return -1;
  }
#else
  if(argc != 3) {
    cout<<"Usage: fluid_sim <input> <hdf_output>";
    return -1;
  }
#endif

  FILE *spec_fp = fopen(argv[1], "r");
  char buf[40960];
  fread(buf, 1, 40960, spec_fp);

  rapidjson::Document spec;
  spec.Parse(buf);

  const size_t height = spec["height"].GetInt();
  const size_t width = spec["width"].GetInt();
  const size_t time = spec["time"].GetInt();
  const double viscosity = spec["viscosity"].GetDouble();

  vector<Splat> splats;

  for(const auto &v : spec["splats"].GetArray()) {
    Splat cur;
    cur.t_from = v["time_from"].GetInt();
    cur.t_to = v["time_to"].GetInt();

    cur.r = v["radius"].GetDouble();

    cur.c.first = v["center"][0].GetDouble();
    cur.c.second = v["center"][1].GetDouble();

    cur.a.first = v["accel"][0].GetDouble();
    cur.a.second = v["accel"][1].GetDouble();

    for(int i = 0; i<3; ++i)
      cur.d[i] = v["dyes"][i].GetDouble();
    splats.push_back(cur);
  }

  cout<<"Read complete"<<endl;

  Simulator sim(height, width, viscosity);

#ifdef ENABLE_GIF
  GifWriter gif;
  GifBegin(&gif, argv[3], width, height, 3, 8, true);

  unique_ptr<uint8_t[]> buffer(new uint8_t[width * height * 4]);
#endif

  for(size_t t = 0; t < time; ++t) {
    cout<<"Time: "<<t<<endl;
    for(const auto &s : splats) {
      if(s.t_from <= t && s.t_to > t)
        sim.splat(s.c, s.r, s.a, s.d);
    }

    sim.step(t);

#ifdef ENABLE_GIF
    sim.write_frame(buffer);
    GifWriteFrame(&gif, buffer.get(), width, height, 3, 8, true);
#endif
  }

  sim.output_hdf(argv[2]);

#ifdef ENABLE_GIF
  GifEnd(&gif);
#endif
}

