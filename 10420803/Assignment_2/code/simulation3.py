#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# Here are the arguments
p=0.3
n=1000
repeat=100
np.random.seed(20231004)

# We define that positive is 1 and negative is 0
positive_count= []
for i in range(0,repeat):
    data = []
    data.append(np.random.choice(a=2,size=n,replace=True,p=[1-p,p]))
    positive_count.append(sum(data[0][0:n]))
average=sum(positive_count)/repeat
print(average)