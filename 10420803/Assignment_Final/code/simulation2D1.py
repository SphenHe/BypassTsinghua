#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

n = 1000000000
np.random.seed(20240107)

data = np.random.choice([-1, 1], (2, n))
data = np.cumsum(data, axis=1)

plt.plot(data[0], data[1])
plt.title('Random Walk')
plt.xlabel('ValueX')
plt.ylabel('ValueY')
plt.grid(True)
plt.show()

print('E(|D|) of data:', np.sqrt(data[0, -1] ** 2 + data[1, -1] ** 2))
print('E(|D|)/sqrt(n) of data:', np.sqrt(data[0, -1] ** 2 + data[1, -1] ** 2) / np.sqrt(n))
