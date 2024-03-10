#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np


n = 10000000
np.random.seed(20240107)

data = np.random.choice([-1, 1], n)
data = np.cumsum(data)

plt.plot(data)
plt.title('Random Walk')
plt.xlabel('Time')
plt.ylabel('Value')
x = np.linspace(0, n, n)
y = np.sqrt(2 * x / np.pi)
plt.plot(x, y)
plt.grid(True)
plt.show()

print('E(|X|) of data:', data[-1])
print('Expected value of E(|X|):', np.sqrt(2 * n / np.pi))
print('(E(|D|)-Expected_E(x))/Expected_E(x) of data:', (data[-1]-np.mean(np.sqrt(2 * n / np.pi))) / np.mean(np.sqrt(2 * n / np.pi)))
