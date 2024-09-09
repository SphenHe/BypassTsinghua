# Fluid std

这是用 C++ 写的标程。和 Python 版本相比，有以下显著的不同：

- Eigen 的 Dense Matrix 是 Column-mojor storage，这个影响了 reshape 之后构造用于求解泊松方程的线性系统中，元素的下标。
- 速度场存储成了 MatrixXd[2]，这是因为 Eigen 只提供了二维矩阵，如果要存储低三个维度，就没有办法 Slice 出来单独一个维度的标量场了。

主文件在 `src/fluid.cpp`

## 编译和执行

你需要安装 meson。除此以外，你需要有合适的 C++ 编译器：以及库。

```bash
sudo pip3 install meson
sudo apt install ninja g++ libhdf5-cpp-103 rapidjson-dev

git submodule update --init --recursive

meson builddir --buildtype=release
ninja -C builddir
```

执行请使用

```
builddir/fluid_std <JSON spec input> <HDF5 output> <GIF output>
```
