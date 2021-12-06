#!/bin/python

with open('input') as f:
#with open('test') as f:
    lines = [line.rstrip() for line in f]

fishes = lines[0].split(',')

fishStates = [0] * 9

i=0
while i < len(fishes):
    fishStates[int(fishes[i])] += 1
    i += 1
#print(fishes)

j=0
while j < 256:
    spawners = fishStates[0]

    i = 1
    while i < len(fishStates):
        fishStates[i-1] = fishStates[i]
        i += 1

    fishStates[6] += spawners
    fishStates[8] =  spawners

    if j == 80-1:
        print('First star:', sum(fishStates))
    if j == 256-1:
        print('Second star:', sum(fishStates))

    j += 1
