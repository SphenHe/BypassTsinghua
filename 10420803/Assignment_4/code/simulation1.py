#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#  Here are the arguments for the function:
mu = 100
sigma = np.sqrt(100)
n = 1000
np.random.seed(20231017)

# normal distribution
data = np.random.normal(mu, sigma, n)

# draw the histogram
plt.hist(data, bins=50, facecolor='green', alpha=0.75)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# randomly pick up 1 sample from data and put it back to the sample and repeat this process for 1000 times
new_data = np.random.choice(data, 1000, replace=True)

# draw the histogram
plt.hist(new_data, bins=50, facecolor='green', alpha=0.75)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# calculate the E(X) and Var(X) of both data and new_data
print('E(X) of data:', np.mean(data))
print('Var(X) of data:', np.var(data))
print('E(X) of new_data:', np.mean(new_data))
print('Var(X) of new_data:', np.var(new_data))

