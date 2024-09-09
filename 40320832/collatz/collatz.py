#!/usr/bin/python3
# -*- coding: utf-8 -*-

n = int(input())

stepCount = 0
maxNum = n

while n != 1:
    if n % 2:
        n = 3 * n + 1
        maxNum=max(int(n),maxNum)
    else:
        n = n // 2
    stepCount += 1

print(stepCount)
print(maxNum)

# TODO: run the loop

# TODO: print total number of step

# TODO: print the max number encountered in the loop
