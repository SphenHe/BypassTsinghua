import numpy as np

DIM = 10


def dist():
    return 0.01


def field():
    xs, ys, zs = np.mgrid[0:DIM, 0:DIM, 0:DIM].astype('float64')

    xs -= (DIM-1) / 2
    ys -= (DIM-1) / 2
    zs -= (DIM-1) / 2

    return np.array([(zs / 2) ** 2, xs ** 2, (zs + ys / 2) ** 2]).transpose((1, 2, 3, 0)) * 0.1


def queries():
    return np.array([
        [3, 5, 8],
        [6, 2, 1],
        [8, 8, 4],
    ])


def ans():
    return (
        np.array([6.640640859609750e-10, -8.411478422172351e-10,
                  2.213546953203250e-10]),
        np.array([[-37.5, -17.5,  30.],
                  [47.5,  17.5, -30.],
                  [-12.5,   2.5, -70.]])
    )
