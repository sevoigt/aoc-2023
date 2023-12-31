"""
day 9
"""

import numpy as np
from functools import reduce


fid = open("input.txt")
lines = fid.readlines()


last_vals = list()
total2 = 0

for history in lines:
    values = np.array([int(i) for i in history.split()])

    first_vals = list()

    while len(values.nonzero()[0]) != 0:
        last_vals.append(values[-1])
        first_vals.append(values[0])
        values = values[1:] - values[:-1]

    total2 += reduce(lambda x, y: y-x, first_vals[::-1])


print("result part 1:", sum(last_vals))
print("result part 2:", total2)
