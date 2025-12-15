import numpy as np
import matplotlib.pyplot as plt

delta_x = 0.01
rho_max  = 1

x_range = 1
t_range = 0.5

delta_t = delta_x/abs((1-2*rho_max))

def relative(x):
    return x + 0.5

rho = np.zeros(x_range/delta_x*t_range/delta_t).reshape(int(x_range/delta_x), int(t_range/delta_t))
for i in range(int(relative(-0.5)/delta_x), int(relative(0)/delta_x)):
    rho[i][0] = 0.3
for i in range(int(relative(0)/delta_x), int(relative(0.5)/delta_x)):
    rho[i][0] = 1

