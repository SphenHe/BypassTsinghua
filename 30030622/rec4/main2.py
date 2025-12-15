import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

# 网格大小
N = 50  # 内部网格点数 (不包括边界)
h = 1.0 / (N + 1)  # 网格步长

# 生成网格点
x = np.linspace(0, 1, N+2)  # 包含边界
y = np.linspace(0, 1, N+2)

# 生成右端项 f(x, y) = -1
F = -np.ones((N, N))

# 生成系数矩阵 A (离散 Laplace 矩阵)
main_diag = -4 * np.ones(N*N)
side_diag = np.ones(N*N-1)
side_diag[np.arange(1, N*N) % N == 0] = 0  # 确保不跨行
up_down_diag = np.ones(N*N-N)

A = sp.diags([main_diag, side_diag, side_diag, up_down_diag, up_down_diag], 
             [0, -1, 1, -N, N], format="csr") / (h*h)

# 右端项转换为列向量
F = F.flatten()

# 计算解
U = spla.spsolve(A, F)

# 恢复到 2D 格式并加上边界条件
U = U.reshape((N, N))
U = np.pad(U, pad_width=1, mode='constant', constant_values=0)

# 可视化结果
import matplotlib.pyplot as plt
plt.imshow(U, extent=[0,1,0,1], origin='lower', cmap='jet')
plt.colorbar(label="u(x, y)")
plt.title("Numerical Solution of 2D Poisson Equation")
plt.show()
