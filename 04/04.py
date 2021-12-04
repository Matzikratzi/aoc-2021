#!/bin/python

with open('input') as f:
#with open('test') as f:
    lines = [line.rstrip() for line in f]

numbers = lines[0].split(',')

# ok, use a list of lists to keep all boards with their numbers. Each
# "outer" element is a list that is a board. In a board, each 5th
# element a new row starts. A column constists of every 5th element.

boards = []

firstDone = False

i = 2
while i < len(lines):
    board = []
    j = i
    while j < i + 5:
        board.extend(lines[j].split())
        j += 1
    i = j + 1
    boards.append(board)

# now we have a list that consists of boards. All in one long
# sequence.
MARKER = 1000000
n = 0
done = False
while n < len(numbers):
    num = numbers[n]
    b = 0
    while b < len(boards):
        board = boards[b]
        if num in board:
            ind = board.index(num)
            board[ind] = MARKER
            row    = ind // 5
            column = ind % 5

            # check if done!
            # row
            c = 0
            done = True
            while c < 5:
                if board[row * 5 + c] != MARKER:
                    done = False
                c += 1
            if done == False:
                # column
                r = 0
                done = True
                while r < 5:
                    if board[r * 5 + column] != MARKER:
                        done = False
                    r += 1
            if done == True:
                i = 0
                while i < len(board):
                    board[i] = int(board[i])
                    i += 1
 
                win = sum(board) * int(num) % MARKER
                if firstDone == False:
                    print('First star: ', win)
                    firstDone = True
                    print('Board: ', b+1)
        b += 1
    n += 1
            
print('Second star: ', win)
print('Board: ', b+1)
