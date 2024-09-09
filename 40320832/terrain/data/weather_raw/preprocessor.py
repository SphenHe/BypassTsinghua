#!/usr/bin/env python3

from scipy.interpolate import griddata, RBFInterpolator, Rbf
import scipy.linalg as linalg
import json
import sys
import math
import numpy as np
import rbf_grid_eval
import matplotlib.pyplot as plt
import gzip


def div_free_rbf(coords, data, epsilon=1):
    coords = np.array(coords)

    def kernel(x1, x2, epsilon=1):
        delta = x2 - x1
        x = delta[0]
        y = delta[1]
        gaussian = math.exp(- epsilon * (x ** 2 + y ** 2))

        return np.array([
            [
                -(4 * (epsilon ** 2) * (y ** 2) - 2 * epsilon) * gaussian,
                4 * x * y * (epsilon ** 2) * gaussian,
            ],
            [
                4 * x * y * (epsilon ** 2) * gaussian,
                -(4 * (epsilon ** 2) * (x ** 2) - 2 * epsilon) * gaussian,
            ],
        ])

    # Solve equations
    b = np.array(data).reshape(-1)
    A = np.zeros((len(coords) * 2, len(coords) * 2), dtype="float64")
    for idx, x in enumerate(coords):
        for ridx, rx in enumerate(coords):
            kn = kernel(x, rx, epsilon)
            A[idx * 2:idx * 2 + 2, ridx * 2:ridx * 2 + 2] = kn
    solved = linalg.solve(A, b)
    cs = solved.reshape(2, -1).T

    return cs


RESOLUTION = 0.002

lon_range = [114.5, 117.5]
lat_range = [38.5, 41.5]


def parse(fd):
    result = {}
    for line in fd.readlines():
        [station, data] = line.split(' ')
        result[station] = float(data)
    return result


stations = json.load(open("./stations.json"))
print("Reading from " + sys.argv[1])
data = parse(open(sys.argv[1]))

vector_mode = len(sys.argv) > 2
if vector_mode:
    angle = parse(open(sys.argv[2]))
    new_data = {}
    for k, v in data.items():
        theta = angle[k] * math.pi / 180
        vector = [v * math.cos(theta), v * math.sin(theta)]
        new_data[k] = vector
    data = new_data

angle = None

data_point = []
coords = []

for k, v in data.items():
    coords.append(stations[k])
    data_point.append(v)

interpolated = None
if not vector_mode:
    grid = np.mgrid[
        lat_range[0]:lat_range[1]:RESOLUTION,
        lon_range[0]:lon_range[1]:RESOLUTION,
    ]
    interpolated = griddata(np.array(coords), data_point,
                            (grid[0], grid[1]), method='cubic')

    (height, width) = interpolated.shape

    SAMPLE_CNT = height
    print(np.nanmax(interpolated))
    print(np.nanmin(interpolated))
    interpolated = np.fmax(0, np.nan_to_num(interpolated, copy=False))
    downsampled = interpolated.reshape(
        (SAMPLE_CNT, int(height / SAMPLE_CNT), SAMPLE_CNT, -1)).mean(axis=(1, 3))
    pltgrid = np.mgrid[
        lat_range[0]:lat_range[1]:(lat_range[1] - lat_range[0])/SAMPLE_CNT,
        lon_range[0]:lon_range[1]:(lon_range[1] - lon_range[0])/SAMPLE_CNT,
    ]
    ctr = plt.contourf(pltgrid[0], pltgrid[1],
                       downsampled, cmap='Blues', levels=20)
    plt.colorbar(ctr)
    plt.savefig('precipitation.jpg')

    with gzip.open('../precipitation.json.gz', 'wt', encoding="ascii") as output:
        json.dump({
            "metadata": {
                "origin": [lat_range[0], lon_range[0]],
                "pixel": [RESOLUTION, RESOLUTION],
            },
            "data": interpolated.tolist(),
        }, output)
else:
    epsilon = 50
    cs = div_free_rbf(coords, data_point, epsilon)
    interpolated = rbf_grid_eval.eval_grid(
        lat_range[0], lat_range[1], RESOLUTION,
        lon_range[0], lon_range[1], RESOLUTION,
        np.array(coords), cs, epsilon
    )

    (height, width, _) = interpolated.shape

    print(np.max(np.abs(interpolated)))

    transposed = interpolated.transpose((2, 0, 1))
    SAMPLE_CNT = 50
    downsampled = transposed.reshape(
        (2, SAMPLE_CNT, int(height / SAMPLE_CNT), SAMPLE_CNT, -1)).mean(axis=(2, 4))
    pltgrid = np.mgrid[
        lat_range[0]:lat_range[1]:(lat_range[1] - lat_range[0])/SAMPLE_CNT,
        lon_range[0]:lon_range[1]:(lon_range[1] - lon_range[0])/SAMPLE_CNT,
    ]

    plt.quiver(pltgrid[0], pltgrid[1], downsampled[0],
               downsampled[1], scale=100)
    plt.savefig('wind.jpg')

    with gzip.open('../wind.json.gz', 'wt', encoding="ascii") as output:
        json.dump({
            "metadata": {
                "origin": [lat_range[0], lon_range[0]],
                "pixel": [RESOLUTION, RESOLUTION],
            },
            "data": interpolated.tolist(),
        }, output)
