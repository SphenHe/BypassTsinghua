import numpy as np

DIM = 10


def dist():
    return 0.01


def field():
    ones = np.ones((DIM, DIM, DIM))
    xs, ys, _ = np.mgrid[0:DIM, 0:DIM, 0:DIM]
    return np.array([ys, -xs, ones]).transpose((1, 2, 3, 0)) * 0.1


def queries():
    return np.array([
        [2, 4, 3],
        [1, 8, 7],
        [6, 4, 5],
    ])


def ans():
    dBdt = np.zeros((3, 3))
    dBdt[:, 2] += 20
    return np.zeros(3), dBdt
