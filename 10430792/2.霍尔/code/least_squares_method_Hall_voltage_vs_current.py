# $I_H$ (mA) & 2.00 & 3.00 & 4.00 & 5.00 & 6.00 & 7.00 & 7.50
# $U_H (mV)$ & 42.0 & 62.8 & 83.6 & 104.6 & 125.4 & 146.0 & 156.3

# read these data, plot them and find the best fit line

import numpy as np
import matplotlib.pyplot as plt

I_H = np.array([2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 7.50])
U_H = np.array([42.0, 62.8, 83.6, 104.6, 125.4, 146.0, 156.3])

# plot the data
plt.plot(I_H, U_H, 'o', label='data')

# find the best fit line
# y = a + b*x
# a = y_mean - b*x_mean
# b = (x*y - x_mean*y_mean) / (x**2 - x_mean**2)
x_mean = np.mean(I_H)
y_mean = np.mean(U_H)
b = np.sum(I_H*U_H - x_mean*y_mean) / np.sum(I_H**2 - x_mean**2)
a = y_mean - b*x_mean
r2 = np.sum((a + b*I_H - y_mean)**2) / np.sum((U_H - y_mean)**2)
print("a = ", a)
print("b = ", b)


# plot the best fit line and add grid, legend, title, axis labels and the equation of the line and R of this line
x = np.linspace(1, 8, 100)
y = a + b*x
plt.plot(x, y, label='best fit line')
plt.grid()
plt.legend()
plt.title("Hall voltage vs current")
plt.xlabel("$I_H$ (mA)")
plt.ylabel("$U_H$ (mV)")
plt.text(4, 60, "$U_H$ = %.2f$I_H$ + %.2f, $r^2$=%.5f" % (b, a, r2))
plt.show()
