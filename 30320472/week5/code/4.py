import matplotlib.pyplot as plt
import numpy as np

# 定义函数
def function(x, k):
    return 0.98 * x / (1 - k * x) - 0.72

# 生成x值的范围
x = np.linspace(0, 3, 400)

# 对k的不同值分别计算y值
k_values = [0, 0.5, 1]
colors = ['blue', 'green', 'red']
plt.figure(figsize=(10, 6))

for k, color in zip(k_values, colors):
    y = function(x, k)
    plt.plot(x, y, label=f'k = {k}', color=color)

plt.title('$Q_E = 0.98 F/F_I / (1 - k F/F_I) - 0.72$')
plt.xlabel('$F/F_I$')
plt.ylabel('$Q_E$')
plt.ylim(0, 20)  # 设置y轴的范围
plt.legend()
plt.grid(True)
plt.savefig('./../img/4.pdf')
# plt.show()
