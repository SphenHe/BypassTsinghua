#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

n = 10000000
np.random.seed(20240107)

theta = np.random.uniform(0, 2 * np.pi, n)
data = np.array([np.cos(theta), np.sin(theta)])
data = np.cumsum(data, axis=1)

plt.plot(data[0], data[1])
plt.title('Random Walk')
plt.xlabel('ValueX')
plt.ylabel('ValueY')
# n = np.linspace(0, n, n)
# x = np.sqrt(n) * np.cos(theta)
# y = np.sqrt(n) * np.sin(theta)
# plt.plot(x, y)
plt.grid(True)
plt.show()

print('E(|D|) of data:', np.sqrt(data[0, -1] ** 2 + data[1, -1] ** 2))
print('Expected value of E(|D|):', np.sqrt(n))
print('(E(|D|)-sqrt(n))/sqrt(n) of data:', (np.sqrt(data[0, -1] ** 2 + data[1, -1] ** 2)-np.sqrt(n)) / np.sqrt(n))
