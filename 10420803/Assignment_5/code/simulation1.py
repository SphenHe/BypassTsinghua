#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#  Here are the arguments for the function:
n = 10000
lambda0 = 1
np.random.seed(20231021)

# Uniform distribution
y_real = np.random.uniform(0, 1, n)

# Exponential distribution
x_real = -np.log(1 - y_real) / lambda0

# Exponential distribution at expected value
x_expectd = np.linspace(0, 10, 1000)

# Plotting the histogram of the exponential distribution
plt.hist(x_real, bins=50, density=True, alpha=0.6, color='g', label='Simulated Data')
plt.plot(x_expectd, lambda0 * np.exp(-lambda0 * x_expectd), 'r-', lw=2, label='Theoretical PDF')
plt.title('Exponential Distribution Probability Density Function')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend(loc='upper right')
plt.show()