'''
画出动能为 1eV 到 10MeV 范围内的电⼦的 $\\beta$ 和 $\gamma$
'''

import numpy as np
import matplotlib.pyplot as plt

# 静止电子的能量(eV)
E_0 = 5.11e5
# 电子的电荷
Q = 1.60217662e-19

# 动能范围
E = np.arange(1, 1e7)

# 速度
B = np.sqrt(1 - (E_0 / (E + E_0))**2)

# $\gamma$
G = 1 / np.sqrt(1 - B**2)

plt.plot(G, B)
plt.xlabel('$\gamma$')
plt.ylabel('$\\beta$')
plt.xscale('log')
plt.yscale('linear')
plt.savefig('./../img/beta_gamma.pdf')
plt.show()
