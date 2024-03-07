# 工作电流$I_H$ (mA) & 0.50 & 1.00 & 1.50 & 2.00 & 2.50 \\\hline
# 电流方向压降$U$ (V) & 0.3796 & 0.7672 & 1.1507 & 1.5286 & 1.9132 \\\hline

# read these data, plot them and find the best fit line

import numpy as np
import matplotlib.pyplot as plt

I_H = np.array([0.50, 1.00, 1.50, 2.00, 2.50])
U = np.array([0.3796, 0.7672, 1.1507, 1.5286, 1.9132])

# plot the data
plt.plot(I_H, U, 'o', label='data')

# find the best fit line
# y = a + b*x
# a = y_mean - b*x_mean
# b = (x*y - x_mean*y_mean) / (x**2 - x_mean**2)
x_mean = np.mean(I_H)
y_mean = np.mean(U)
b = np.sum(I_H*U - x_mean*y_mean) / np.sum(I_H**2 - x_mean**2)
a = y_mean - b*x_mean
r2 = np.sum((a + b*I_H - y_mean)**2) / np.sum((U - y_mean)**2)
print("a = ", -a)
print("b = ", b)


# plot the best fit line and add grid, legend, title, axis labels and the equation of the line and R of this line
x = np.linspace(0, 3, 100)
y = a + b*x
plt.plot(x, y, label='best fit line')
plt.grid()
plt.legend()
plt.title("U vs $I_H$")
plt.xlabel("$I_H$ (mA)")
plt.ylabel("$U$ (V)")
plt.text(1, 0.5, "$U$ = %.2f$I_H$ + %.2f, $r^2$=%.5f" % (b, -a, r2))
plt.show()
