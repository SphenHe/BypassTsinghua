# $I_M$ (mA) & 0 & 100 & 200 & 300 & 400 & 500 & 600 & 700 & 800 & 900 & 1000 \\\hline
# $B$ (mT) & 0.1 & 23.5 & 48.5 & 73.0 & 97.2 & 121.3 & 145.6 & 169.5 & 193.0 & 216.7 & 240.0 \\\hline

# read these data, plot them and find the best fit line

import numpy as np
import matplotlib.pyplot as plt

# read the data
I_H = np.array([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) * 1e-3
B= np.array([0.1, 23.5, 48.5, 73.0, 97.2, 121.3, 145.6, 169.5, 193.0, 216.7, 240.0]) * 1e-3

# plot the data
# plt.scatter(I_H, B, label='data')
plt.plot(I_H, B, 'o', label='data')

# find the best fit line
# y = a + b*x
# a = y_mean - b*x_mean
# b = (x*y - x_mean*y_mean) / (x**2 - x_mean**2)
x_mean = np.mean(I_H)
y_mean = np.mean(B)
b = np.sum(I_H*B - x_mean*y_mean) / np.sum(I_H**2 - x_mean**2)
a = y_mean - b*x_mean
r2 = np.sum((a + b*I_H - y_mean)**2) / np.sum((B - y_mean)**2)
print("a = ", a)
print("b = ", b)

# plot the best fit line and add grid, legend, title, axis labels and the equation of the line and R of this line
x = np.linspace(0, 1, 100)
y = a + b*x
plt.plot(x, y, label='best fit line')
plt.grid()
plt.legend()
plt.title("Magnetic field vs current")
plt.xlabel("$I_M$ (mA)")
plt.ylabel("$B$ (mT)")
plt.text(0.5, 0.1, "$B$ = %.2f$I_M$ + %.2f, $r^2$=%.5f" % (b, a, r2))
plt.show()