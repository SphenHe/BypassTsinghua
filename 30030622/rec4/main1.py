import numpy as np
import matplotlib.pyplot as plt

# 2D Possion Equation

n = 100

f = np.ones(n**2)

A = np.zeros((n**2, n**2))

for i in range(n**2):
    A[i][i] = 4
    if i + 1 < n**2:
        A[i][i+1] = -1
    if i - 1 >= 0:
        A[i][i-1] = -1
    if i + n < n**2:
        A[i][i+n] = -1
    if i - n >= 0:
        A[i][i-n] = -1

A[0][0] = 2
A[-1][-1] = 2

u = np.linalg.solve(A, f)
u = u.reshape(n, n)

plt.imshow(u, cmap='hot', interpolation='nearest')

print(u)
