# %%
import numpy as np

# 2D Possion Equation

n = 10

f = np.ones(n**3)

A = np.zeros((n**3, n**3))

for i in range(n**3):
    A[i][i] = 6
    if (i + 1) % n != 0 and (i + 1) < n**3:
        A[i][i + 1] = -1
    if i % n != 0 and (i - 1) >= 0:
        A[i][i - 1] = -1
    if (i + n) % (n**2) < n**2 and (i + n) < n**3:
        A[i][i + n] = -1
    if (i - n) >= 0:
        A[i][i - n] = -1
    if (i + n**2) < n**3:
        A[i][i + n**2] = -1
    if (i - n**2) >= 0:
        A[i][i - n**2] = -1

A = A * (n**3)

print(A)


# %%
u = np.linalg.solve(A, f)

# %%
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = u.reshape((n, n, n))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, n), np.linspace(0, 1, n))

scat = ax.scatter(x, y, z, c=u.flatten(), cmap='jet')
plt.colorbar(scat, ax=ax, shrink=0.5, aspect=5)
plt.title('3D Poisson Equation')
plt.savefig('3D_Poisson.png', dpi=500)
plt.show()

print(u)



