import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt

# 网格大小
N = 20  # 3D 内部网格点数 (不包括边界)
h = 1.0 / (N + 1)  # 网格步长

# 生成右端项 f(x, y, z) = -1
F = -np.ones((N, N, N))

# 生成稀疏矩阵 A（3D Laplacian 离散化）
main_diag = -6 * np.ones(N**3)
xyz_diag = np.ones(N**3-1)
xyz_diag[np.arange(1, N**3) % N == 0] = 0  # 确保不跨行
up_down_diag = np.ones(N**3 - N)
z_diag = np.ones(N**3 - N**2)

A = sp.diags([main_diag, xyz_diag, xyz_diag, up_down_diag, up_down_diag, z_diag, z_diag], 
             [0, -1, 1, -N, N, -N**2, N**2], format="csr") / (h*h)

# 右端项转换为列向量
F = F.flatten()

# 计算解
U = spla.spsolve(A, F)

# 恢复为 3D 格式并加上边界条件
U = U.reshape((N, N, N))
U = np.pad(U, pad_width=1, mode='constant', constant_values=0)

# 可视化 3D 结果（绘制某一层切片）
z_slice = N // 2  # 取 z = 0.5 处的切片
plt.imshow(U[:, :, z_slice], extent=[0,1,0,1], origin='lower', cmap='jet')
plt.colorbar(label="u(x, y, z)")
plt.title(f"3D Poisson Equation Solution (z={z_slice/N:.2f})")
plt.show()
