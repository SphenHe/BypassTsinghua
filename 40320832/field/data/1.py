import numpy as np

DIM = 10


def dist():
    return 0.01


def field():
    ones = np.ones((DIM, DIM, DIM))
    return np.array([ones * 0.3, ones * 0.2, ones * 0.1]).transpose((1, 2, 3, 0))


def queries():
    return np.array([
        [1, 1, 1],
        [3, 1, 4],
        [6, 6, 6],
    ])


def ans():
    return np.zeros(3), np.zeros((3, 3))
