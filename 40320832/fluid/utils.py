# Provided functions. DO NOT CHANGE THIS FILE!

import numpy as np
from scipy.sparse import csc_matrix, identity
from scipy.sparse.linalg import factorized

def build_diffusor(height, width, boundary_scale, self_factor = 1):
    def coord(i, j):
        return i * width + j

    data = []
    row = []
    col = []

    for i in range(0, height):
        for j in range(0, width):
            curidx = coord(i, j)

            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                data.append(self_factor)
                row.append(curidx)
                col.append(curidx)
                continue

            self_total = -4
            for (di, dj) in ((1, 0), (0, -1), (-1, 0), (0, 1)):
                ni = i + di
                nj = j + dj
                if ni == 0 or ni == height - 1 or nj == 0 or nj == width - 1:
                    self_total += boundary_scale
                else:
                    data.append(1)
                    row.append(curidx)
                    col.append(coord(ni, nj))

            data.append(self_total)
            row.append(curidx)
            col.append(curidx)

    cnt = width * height
    return csc_matrix((data, (row, col)), shape=(cnt, cnt), dtype=np.double)

def build_poisson_solver(height, width, r, s, factor):
    mat = build_diffusor(height, width, factor, 1 - r / s)
    mat2 = identity(height * width, format = "csc") * r + mat * s
    return factorized(mat2)
