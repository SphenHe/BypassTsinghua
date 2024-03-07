# 序号 & 起偏器检偏器夹角$\theta$ (°) & 相对透过率 $(I_m- I_0)/ (I_{max}- I_0)$ & $\cos^2\theta$
# 1 & 0.0 ($I_{max}$) & 1.0000 & 1.0000
# 2 & 15.0 & 0.9346 & 0.9330
# 3 & 30.0 & 0.7523 & 0.7500
# 4 & 45.0 & 0.5040 & 0.5000
# 5 & 60.0 & 0.2500 & 0.2500
# 6 & 75.0 & 0.0666 & 0.0699
# 7 & 80.0 & 0.0315 & 0.0302
# 8 & 84.0 & 0.0123 & 0.0109
# 9 & 87.0 & 0.0025 & 0.0027
# 10 & 90.0 & 0.0000 & 0.0000

# data1: relative transmission rate vs theta
# data2: Im cos^2(theta) vs theta

# read these data, plot them and link them with a smooth curve

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# read the data
theta = np.array([0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 80.0, 84.0, 87.0, 90.0])
n = np.array([1.0000, 0.9346, 0.7523, 0.5040, 0.2500, 0.0666, 0.0315, 0.0123, 0.0025, 0.0000])
cos2 = np.array([1.0000, 0.9330, 0.7500, 0.5000, 0.2500, 0.0699, 0.0302, 0.0109, 0.0027, 0.0000])

# plot the data
plt.plot(theta, n, 'o', label='data_real')
plt.plot(theta, cos2, 'o', label='data_expected')

# link the data with a smooth curve
theta_smooth = np.linspace(0, 90, 100)

# cos2_smooth = np.interp(theta_smooth, theta, cos2)
# n_smooth = np.interp(theta_smooth, theta, n)

# create interpolation functions
f_cos2 = interp1d(theta, cos2, kind='quadratic')
f_n = interp1d(theta, n, kind='quadratic')

# use the interpolation functions to create smooth curves
cos2_smooth = f_cos2(theta_smooth)
n_smooth = f_n(theta_smooth)

plt.plot(theta_smooth, n_smooth, label='smooth_curve_real')
plt.plot(theta_smooth, cos2_smooth, label='smooth_curve_expected')

plt.grid()
plt.legend()
plt.title("relative transmission rate vs theta")
plt.xlabel("$theta$ (°)")
plt.ylabel("relative transmission rate")
plt.show()
