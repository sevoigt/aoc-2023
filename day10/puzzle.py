"""
day 10
"""

import numpy as np


# navigation dict, example: coming from 'S' (for south) and
# finding a '7' means: stay in row and go one column left,
# the next cell you enter is from 'E' (for east); repeat

navi = {'N' : {'L' : ((0,  1), 'W'),
               'J' : ((0, -1), 'E'),
               '|' : ((1,  0), 'N')},

        'E' : {'F' : (( 1,  0), 'N'),
               'L' : ((-1,  0), 'S'),
               '-' : (( 0, -1), 'E')},

        'S' : {'7' : (( 0, -1), 'E'),
               'F' : (( 0,  1), 'W'),
               '|' : ((-1,  0), 'S')},

        'W' : {'7' : (( 1, 0), 'N'),
               'J' : ((-1, 0), 'S'),
               '-' : (( 0, 1), 'W')}}



fid = open("input.txt")
lines = fid.readlines()

# read grid and find start position
grid = np.array([list(i) for i in lines])
start = [int(i[0]) for i in np.where(grid == 'S')]
start = np.array(start)

steps = 0

# find first element of path after start and how we got there
for move in (('S', (-1,0)), ('W', (0,1)), ('N', (1,0)), ('E', (0, -1))):
    from_dir = move[0]
    direction = move[1]
    pos = start + direction
    steps += 1
    if grid[tuple(pos)] in navi[from_dir].keys():
        break


while not np.array_equal(pos, start):

    move = navi[from_dir][grid[tuple(pos)]]
    pos = np.array(pos) + move[0]
    from_dir = move[1]

    steps += 1

print('result part 1:', int(steps/2))
