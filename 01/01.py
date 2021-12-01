#!/bin/python

import numpy as np

depths = np.loadtxt('input_01_1.txt', dtype=int)
#depths = np.loadtxt('test_input_1.txt', dtype=int)

d0 = depths[0:depths.size-1]
d1 = depths[1:depths.size]

diffs = np.subtract(d1, d0)

count = 0
increasing = 0

while count < len(diffs):
    if diffs[count] > 0:
        increasing += 1
    count += 1

print('First Star: ', increasing)

################################################################################

d0 = depths[0:depths.size-2]
d1 = depths[1:depths.size-1]
d2 = depths[2:depths.size]

dFilt = np.add(d0, d1)
dFilt = np.add(dFilt, d2)

print(dFilt)

diffsFilt = np.subtract(dFilt[1:], dFilt[0:dFilt.size-1])

count = 0
increasing = 0

while count < len(diffsFilt):
    if diffsFilt[count] > 0:
        increasing += 1
    count += 1

print('Second Star: ', increasing)

