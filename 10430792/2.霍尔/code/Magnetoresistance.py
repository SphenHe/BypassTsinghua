# $B$ (mT) & 0.0 & 12.0 & 24.0 & 36.0 & 48.0 & 60.0 & 72.0 & 84.0 \\\hline
# $\Delta R/R(0)$ & 0.0000 & 0.0132 & 0.0497 & 0.1071 & 0.1788 & 0.2658 & 0.3508 & 0.4358 \\\hline
# $B$ (mT) & 96.0 & 120.0 & 144.0 & 168.0 & 192.0 & 216.0 & 240.0 & \~{} \\\hline
# $\Delta R/R(0)$ & 0.5015 & 0.5912 & 0.6580 & 0.7196 & 0.7822 & 0.8296 & 0.8882 & \~{} \\\hline


# read these data, plot them and link them with a smooth curve

import numpy as np
import matplotlib.pyplot as plt

# read the data
B = np.array([0.0, 12.0, 24.0, 36.0, 48.0, 60.0, 72.0, 84.0, 96.0, 120.0, 144.0, 168.0, 192.0, 216.0, 240.0])
R = np.array([0.0000, 0.0132, 0.0497, 0.1071, 0.1788, 0.2658, 0.3508, 0.4358, 0.5015, 0.5912, 0.6580, 0.7196, 0.7822, 0.8296, 0.8882])

# plot the data
plt.plot(B, R, 'o', label='data')

# link the data with a smooth curve
B_smooth = np.linspace(0, 240, 100)
R_smooth = np.interp(B_smooth, B, R)
plt.plot(B_smooth, R_smooth, label='smooth curve')

plt.grid()
plt.legend()
plt.title("R vs B")
plt.xlabel("$B$ (mT)")
plt.ylabel("$\Delta R/R(0)$")
plt.show()

