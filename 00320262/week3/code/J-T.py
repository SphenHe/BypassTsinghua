import numpy as np
import matplotlib.pyplot as plt

# 定义常量
k = 8.617333262145e-5  # eV/K
A = 1.202e6  # A/m^2/K^2

# 定义温度范围 (K)
T = np.linspace(373, 2273, 500)

# 定义材料的功函数 (eV)
materials = {
    'Cu': 4.65,
    'Au': 5.10,
    'Ag': 4.26,
    'W': 4.55,
    'LaB6': 2.70
}

# 计算电流密度
def current_density(T, phi):
    return A * T**2 * np.exp(-phi / (k * T))

# 绘制曲线
plt.figure(figsize=(10, 6))

for material, phi in materials.items():
    J = current_density(T, phi)
    plt.plot(T - 273.15, J, label=material)  # 转换为摄氏度

plt.yscale('log')
plt.xlabel('Temperature (°C)')
plt.ylabel('Thermal emission current density (A/m^2)')
plt.title('Thermal emission current density of different materials')
plt.legend()
plt.grid(True)
plt.savefig('./../img/J-T.pdf')
# plt.show()
