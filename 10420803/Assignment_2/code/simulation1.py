#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# Here are the arguments
p=0.3
n=1000
np.random.seed(20231004)

# We define that positive is 1 and negative is 0
data = []
data.append(np.random.choice(a=2,size=n,replace=True,p=[1-p,p]))
N = np.arange(1,n+1)
# Calculate the relative frequency
relative_frequency= []
for i in range(0,n):
    relative_frequency.append(sum(data[0][0:i])/(i+1))

# Draw Scatter plot using matplotlib.pyplot
plt.style.use("ggplot")
font = {"family": "Times New Roman",
        "weight": "normal",
        "size": 12}
plt.scatter(x=N, y=relative_frequency, c="blue",label="relative_frequency")
plt.xlabel("N", font)
plt.ylabel("relative_frequency", font)
plt.title("relative_frequency-N", font)
plt.legend(prop=font)
plt.show()