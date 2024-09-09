import numpy as np

DIM = 10


def dist():
    return 0.01


def field():
    return np.mgrid[0:DIM, 0:DIM, 0:DIM].transpose((1, 2, 3, 0)) * 0.1


def queries():
    return np.array([
        [1, 3, 1],
        [7, 2, 6],
        [5, 5, 5],
    ])


def ans():
    return np.ones(3) * 2.6562563438439e-10, np.zeros((3, 3))
