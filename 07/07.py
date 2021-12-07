#!/bin/python

import numpy as np

def fuel(diff, part):
    f = 0
    for d in diff:
        if part == 1:
            f += d
        else:
            f += int((d + 1)*d/2)
    return f
        

with open('input') as f:
#with open('test') as f:
    lines = [line.rstrip() for line in f]

depths = np.fromstring(lines[0], dtype=int, sep=',')

part_1_min_fuel = 1000000000
part_2_min_fuel = 1000000000
i = min(depths)
while i <= max(depths):
    f1 = fuel(abs(depths - i), 1)
    if f1 < part_1_min_fuel:
        part_1_min_fuel = f1

    f2 = fuel(abs(depths - i), 2)
    if f2 < part_2_min_fuel:
        part_2_min_fuel = f2
    i += 1

print(part_1_min_fuel)
print(part_2_min_fuel)



