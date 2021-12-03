#!/bin/python

import math

with open('input') as f:
#with open('test') as f:
    lines = [line.rstrip() for line in f]

bin1 = [0]*len(lines[0])
    
i = 0
while i < len(lines):
    diag = lines[i]
    pos = 0
    while pos < len(diag):
        if diag[pos] == '1':
           bin1[pos] += 1
        pos += 1
    i += 1

    
gamma = 0
epsilon = 0

pos = 0
while pos < len(diag):
    gamma *= 2
    epsilon *= 2
    if bin1[pos] > len(lines)/2:
        gamma += 1
    else:
        epsilon += 1
    pos += 1

print('First star: ', gamma *  epsilon)


################################################################################

lines.sort()

c_max = len(lines[0])

#### oxygen

r_min = 0
r_max = len(lines)

c = 0
while c < c_max:
    r_num = r_max - r_min
    r = r_min

    while r < r_max:
        if lines[r][c] == '1':
            if (r - r_min) <= (r_max - r):
                r_min = r
                r = r_max
            else:
                if (r - r_min) > (r_max - r):
                    r_max = r
                    r = r_max
        else:
            r += 1
    c += 1

oxygen = int(lines[r_min], 2)

#### co2

r_min = 0
r_max = len(lines)

c = 0
while c < c_max:
    r_num = r_max - r_min
    r = r_min

    while r < r_max:
        if lines[r][c] == '1':
            if (r - r_min) > (r_max - r):
                r_min = r
                r = r_max
            else:
                if (r - r_min) <= (r_max - r):
                    r_max = r
                    r = r_max
        else:
            r += 1
    c += 1

co2 = int(lines[r_min], 2)

print('Second star: ', oxygen * co2)
