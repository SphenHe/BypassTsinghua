import matplotlib.pyplot as plt
import numpy as np

# 定义参数 a 和 b
a = 1
b = 1.5

# 创建图形
fig, ax = plt.subplots()

# 绘制 x 的范围
ax.axvline(-2*a, color='k', linestyle='--')
ax.axvline(2*a, color='k', linestyle='--')

# 绘制 y 的范围
ax.axhline(-b, color='k', linestyle='--')
ax.axhline(b, color='k', linestyle='--')

# 绘制 y = |x| * (b/a) 和 y = -|x| * (b/a) 的直线
x = np.linspace(-2*a, 2*a, 1000)
y_upper = np.abs(x) * (b/a)
y_lower = -np.abs(x) * (b/a)

ax.plot(x, y_upper, 'k')
ax.plot(x, y_lower, 'k')

# 填充符合条件的区域 |y| > |x|
x_fill = np.linspace(-2*a, 2*a, 1000)
y_fill_upper = np.abs(x_fill) * (b/a)
y_fill_lower = -np.abs(x_fill) * (b/a)

ax.fill_between(x_fill, y_fill_upper, y_fill_lower, where=(np.abs(y_fill_lower) < np.abs(x_fill)), color='lightblue', alpha=0.5)

# 设置 x 和 y 的限制
ax.set_xlim(-3*a, 3*a)
ax.set_ylim(-1.5*b, 1.5*b)

# 设置坐标轴标签
ax.set_xlabel('x')
ax.set_ylabel('x\'')

# 显示图形
plt.show()
