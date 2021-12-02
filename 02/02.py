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

print('forward ', dir_forward)
print('down ', dir_down)
print('up ', dir_up)

print('First star: ', dir_forward * (dir_down - dir_up))
