#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from scipy import stats
from scipy.special import comb

# Here are the arguments
p=0.6
n=25
np.random.seed(20231004)

# Calculate the possibility of each case
data_p = []
for i in range (0,n+1):
    data_p.append(comb(25,i)*p**i*(1-p)**(25-i))

# Find the maximum possibility
max = 0
for i in range (0,n+1):
    if data_p[i] > max:
        max = data_p[i]
        index = i
print("The maximum possibility is", max, "when i =", index)

# Calculate the mathematical expectation \mu
E = 0
for i in range (0,n+1):
    E = E + i*data_p[i]
print("The mathematical expectation is", E)

# Calculate the variance \sigma^2
Var = 0
for i in range (0,n+1):
    Var = Var + (i-E)**2*data_p[i]
print("The variance is", Var)

# Calculate the possibility of \mu-2\sigma<x<\mu+2\sigma
Possibility = 0
for i in range (int(E-2*np.sqrt(Var))+1,int(E+2*np.sqrt(Var))+1):
    Possibility = Possibility + data_p[i]
print("The possibility of $\mu-2\sigma<x<\mu+2\sigma$ is", Possibility)

# Plot the possibility mass function graph
x_p = np.arange(26)
custm = stats.rv_discrete(name='custm', values=(x_p, data_p))

fig, ax = plt.subplots(1, 1)
ax.plot(x_p, custm.pmf(x_p), 'ro', ms=8, mec='r')
ax.vlines(x_p, 0, custm.pmf(x_p), colors='r', linestyles='-', lw=2)
plt.xlabel('i')
plt.ylabel('Possibility')
plt.title('Possibility Mass Function')
plt.show()