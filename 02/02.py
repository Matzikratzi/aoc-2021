#!/bin/python

import math

with open('input_02_1.txt') as f:
#with open('test') as f:
    lines = [line.rstrip() for line in f]

dir_forward = 0
dir_down = 0
dir_up = 0

i = 0

while i < len(lines):
    cmdLine = lines[i]
    direction, numeric = cmdLine.split()
    num = int(numeric)
    if direction == 'forward':
        dir_forward += num
    if direction == 'up':
        dir_up += num
    if direction == 'down':
        dir_down += num
    
    i += 1

print('First star: ', dir_forward * (dir_down - dir_up))

################################################################################


horizontal = 0
depth = 0
aim = 0

i = 0

while i < len(lines):
    cmdLine = lines[i]
    direction, numeric = cmdLine.split()
    num = int(numeric)

    if direction == 'forward':
        horizontal += num
        depth += aim * num
    if direction == 'up':
        aim -= num
    if direction == 'down':
        aim += num
    
    i += 1

print('Second star: ', horizontal * depth)
