#!/bin/python

import re

# a in nums: 8
# b in nums: 6
# c in nums: 8
# d in nums: 7
# e in nums: 4
# f in nums: 9
# g in nums: 7

# br is the one that is found 6 times
# fr is the one that is found 9 times
# er is the one that is found 4 times
# cr is the one found together with only f
# ar is the one with 8 times that is not c # a is the one found together with c and f
# dr is the one found with three others that is not b, c or f
# gr is the one found with a, c, d, f

def split(word):
    return [char for char in word]

# coded is a list of led-strings, keys is a hashmap "coded to real"
def decipher(coded, keys):
    n = 0
    for code in coded:
        rl = []
        for l in code:
            rl.append(keys[l])
            rl.sort()
        r = "".join(rl)
        #print(r)
        n *= 10
        if r == 'abcefg':
            n += 0
        elif r == 'cf':
            n += 1
        elif r == 'acdeg':
            n += 2
        elif r == 'acdfg':
            n += 3
        elif r == 'bcdf':
            n += 4
        elif r == 'abdfg':
            n += 5
        elif r == 'abdefg':
            n += 6
        elif r == 'acf':
            n += 7
        elif r == 'abcdefg':
            n += 8
        elif r == 'abcdfg':
            n += 9
        else:
            print('Big error!')
            n = 1000000000000000
    return n

def find_rs(leds):
    s = "".join(leds)
    c = 'abcdefg'

    keys = {}
    reverse = {}
    i = 0
    while i<len(c):
        wire = c[i]
        if s.count(wire) == 6:
           keys[wire] = 'b'
           reverse['b'] = wire

        if s.count(wire) == 9:
           keys[wire] = 'f'
           reverse['f'] = wire


        if s.count(wire) == 4:
           keys[wire] = 'e'
           reverse['e'] = wire

        i += 1

    i = 0
    while i < len(leds):
        l = leds[i]
        if len(l) == 2:
            wire = l.replace(reverse['f'], '')
            keys[wire] = 'c'
            reverse['c'] = wire
            #print(l)
        i += 1
    
    i = 0
    while i < len(leds):
        l = leds[i]
        if len(l) == 3:
            wires = l.replace(reverse['f'], '')
            wire = wires.replace(reverse['c'], '')
            keys[wire] = 'a'
            reverse['a'] = wire
            #print(l)
        i += 1

    i = 0
    while i < len(leds):
        l = leds[i]
        if len(l) == 4:
            wires = l.replace(reverse['f'], '')
            wires = wires.replace(reverse['b'], '')
            wire = wires.replace(reverse['c'], '')
            keys[wire] = 'd'
            reverse['d'] = wire
            #print(l)
        i += 1

    i = 0
    while i < len(leds):
        l = leds[i]
        if (len(l) == 5) and re.search(reverse['c'], l) and re.search(reverse['f'], l):
            wires = l.replace(reverse['a'], '')
            wires = wires.replace(reverse['c'], '')
            wires = wires.replace(reverse['d'], '')
            wire = wires.replace(reverse['f'], '')
            keys[wire] = 'g'
            reverse['g'] = wire
            #print(l)
        i += 1

    return keys
    

with open('input') as f:
#with open('test') as f:
    lines = [line.rstrip() for line in f]

count = 0
i = 0
while i < len(lines):
    sides = lines[i].split(' | ')
    ns = sides[1].split(' ')
    #print(ns)
    for s in ns:
        l = len(s)
        if l == 2 or l == 3 or l == 4 or l == 7:
            count += 1
    i += 1

print('First star: ', count)







summa = 0
i = 0
while i < len(lines):
    line = lines[i]
    i += 1
    sides = line.split(' | ')
    leds = sides[0].split()
    keys = find_rs(leds)
    #print(keys)

    coded_leds = sides[1].split()
    num = decipher(coded_leds, keys)
    summa += num

print('Second star: ', summa)
