"""
day 11
"""

import numpy as np


def expand(universe):
    """
    Fill in empty rows - not smart but totally fine for small problem
    """

    expanded = list()

    for row in universe:
        expanded.append(row)
        if len(row[row=='.']) == len(row):
            expanded.append(row)

    return np.array(expanded)


def find_empty(universe):
    """
    Find only indices of empty rows
    """

    idx = list()

    for i, row in enumerate(universe):
        if len(row[row=='.']) == len(row):
            idx.append(i)

    return idx



fid = open("input.txt")
lines = fid.readlines()


# read and expand grid, find galaxies
grid = np.array([list(i.strip()) for i in lines])

grid = expand(grid)
grid = expand(grid.transpose()).transpose()

galaxies = np.vstack(np.where(grid == '#')).transpose()


# part 1

distance = 0

for i in range(1, len(galaxies)):
    for k in range(0, i):
        distance += sum(abs(galaxies[i]-galaxies[k]))

print('result part 1:', distance)



# part 2 - reset grid and galaxies first

grid = np.array([list(i.strip()) for i in lines])
galaxies = np.vstack(np.where(grid == '#')).transpose()

row_idx = find_empty(grid)
col_idx = find_empty(grid.transpose())

distance2 = 0

for i in range(1, len(galaxies)):
    for k in range(0, i):

        distance2 += sum(abs(galaxies[i]-galaxies[k]))

        r1 = galaxies[i][0]
        r2 = galaxies[k][0]

        c1 = galaxies[i][1]
        c2 = galaxies[k][1]

        for r in row_idx:
            if min(r1, r2) < r < max(r1, r2):
                distance2 += 999999

        for c in col_idx:
            if min(c1, c2) < c < max(c1, c2):
                distance2 += 999999

print('result part 2:', distance2)


