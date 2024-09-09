use pyo3::prelude::*;
use ndarray::{Array3, Array2};
use numpy::{IntoPyArray, PyArray3, PyReadonlyArray2};
use rayon::iter::ParallelIterator;
use rayon::iter::IntoParallelIterator;

fn kernel_mut([dx, dy]: [f64; 2], c: [f64; 2], epsilon: f64) -> [f64; 2] {
    let gaussian = std::f64::consts::E.powf(- epsilon * (dx * dx + dy * dy));

    let mat = [
        [
            -(4f64 * (epsilon * epsilon) * (dy * dy) - 2f64 * epsilon) * gaussian,
            4f64 * dx * dy * (epsilon * epsilon) * gaussian,
        ],
        [
            4f64 * dx * dy * (epsilon * epsilon) * gaussian,
            -(4f64 * (epsilon * epsilon) * (dx * dx) - 2f64 * epsilon) * gaussian,
        ],
    ];

    [
        mat[0][0] * c[0] + mat[0][1] * c[1],
        mat[1][0] * c[0] + mat[1][1] * c[1],
    ]
}

fn eval_on([x, y]: [f64; 2], refs: &[([f64; 2], [f64; 2])], epsilon: f64) -> [f64; 2] {
    let mut result = [0f64, 0f64];
    for ([rx, ry], c) in refs {
        let cur = kernel_mut([x - rx, y - ry], *c, epsilon);
        result[0] += cur[0];
        result[1] += cur[1];
    }
    result
}

fn eval_grid_impl(
    x_from: f64,
    x_to: f64,
    x_step: f64,
    y_from: f64,
    y_to: f64,
    y_step: f64,
    refs: &[([f64; 2], [f64; 2])],
    epsilon: f64,
) -> Array3<f64> {
    let height = ((x_to - x_from) / x_step) as usize;
    let width = ((y_to - y_from) / y_step) as usize;

    let array: Array2<f64> = (0..height).into_par_iter().map(
        |i| {
            (0..width).map(|j| {
                let x = i as f64 * x_step + x_from;
                let y = j as f64 * y_step + y_from;
                eval_on([x, y], refs, epsilon)
            }).collect::<Vec<_>>()
        }
    ).flatten().collect::<Vec<_>>().into();

    array.into_shape((height, width, 2)).unwrap()
}

#[pymodule]
fn rbf_grid_eval(_py: Python, m: &PyModule) -> PyResult<()> {

    #[pyfn(m, "eval_grid")]
    fn eval_grid<'py>(
        py: Python<'py>,

        x_from: f64,
        x_to: f64,
        x_step: f64,
        y_from: f64,
        y_to: f64,
        y_step: f64,

        coords: PyReadonlyArray2<f64>,
        cs: PyReadonlyArray2<f64>,

        epsilon: f64,
    ) -> &'py PyArray3<f64> {
        let ref_cnt = coords.shape()[0];
        let mut refs = Vec::with_capacity(ref_cnt);
        for i in 0..ref_cnt {
            refs.push((
                [*coords.get((i, 0)).unwrap(), *coords.get((i, 1)).unwrap()],
                [*cs.get((i, 0)).unwrap(), *cs.get((i, 1)).unwrap()],
            ));
        }
        
        let grid = eval_grid_impl(x_from, x_to, x_step, y_from, y_to, y_step, refs.as_slice(), epsilon);
        grid.into_pyarray(py)
    }
    Ok(())
}
