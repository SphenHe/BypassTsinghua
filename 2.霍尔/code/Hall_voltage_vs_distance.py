# $x$ (mm) & 0.0 & 4.0 & 6.0 & 8.0 & 10.0 & 12.0 & 17.0 & 22.0 \\\hline
# $B$ (mT) & 51.7 & 83.7 & 104.7 & 117.2 & 121.4 & 122.2 & 122.2 & 121.8 \\\hline
# $x$ (mm) & 28.0 & 33.0 & 38.0 & 40.0 & 42.0 & 44.0 & 46.0 & 50.0\\\hline
# $B$ (mT) & 121.4 & 120.9 & 120.5 & 120.1 & 118.5 & 113.2 & 99.8 & 65.8 \\\hline

# read these data, plot them and link them with a smooth curve

import numpy as np
import matplotlib.pyplot as plt

# read the data
x = np.array([0.0, 4.0, 6.0, 8.0, 10.0, 12.0, 17.0, 22.0, 28.0, 33.0, 38.0, 40.0, 42.0, 44.0, 46.0, 50.0])
B = np.array([51.7, 83.7, 104.7, 117.2, 121.4, 122.2, 122.2, 121.8, 121.4, 120.9, 120.5, 120.1, 118.5, 113.2, 99.8, 65.8])

# plot the data
plt.plot(x, B, 'o', label='data')

# link the data with a smooth curve
x_smooth = np.linspace(0, 50, 100)
B_smooth = np.interp(x_smooth, x, B)
plt.plot(x_smooth, B_smooth, label='smooth curve')

plt.grid()
plt.legend()
plt.title("B vs x")
plt.xlabel("$x$ (mm)")
plt.ylabel("$B$ (mV)")
plt.show()
