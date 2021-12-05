#!/bin/python

def solver(part):

    with open('input') as f:
    #with open('test') as f:
        lines = [line.rstrip() for line in f]

    # The 1000*1000 matrix is represented by an array [0 .. 999999]

    matrix_width = 1000

    matrix = [0] * matrix_width * matrix_width

    i = 0
    while i < len(lines):
        line = lines[i]
        coord1, coord2 = line.split(' -> ')
        x1, y1 = coord1.split(',')
        x2, y2 = coord2.split(',')
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)

        if x1 > x2:
            tmp = x2
            x2 = x1
            x1 = tmp
            tmp = y2
            y2 = y1
            y1 = tmp

        if x1 != x2:
            if y1 == y2:
                k = 0
            elif y1 < y2:
                k = 1
            else:
                k = -1

            while x1 <= x2:
                if k == 0 or part == 2:
                    matrix[x1 + y1 * matrix_width] += 1
                x1 += 1
                y1 += k

        else:
            if y1 > y2:
                tmp = y2
                y2 = y1
                y1 = tmp

            while y1 <= y2:
                matrix[x1 + y1 * matrix_width] += 1
                y1 += 1
        i +=1

    pind=0
    while pind < matrix_width:
        pind += 1

    points = 0

    j = 0

    while j < len(matrix):
        if matrix[j] > 1:
            points +=1
        j += 1
    return points

ps = solver(1)
print('First star: ', ps)

ps = solver(2)
print('Second star: ', ps)
