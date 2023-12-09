"""
day 9
"""

import numpy as np
from functools import reduce


def get_numbers(line):
    """
    Get list of integer space-separated numbers from string
    """
    return [int(i) for i in line.split()]


fid = open("input.txt")
lines = fid.readlines()



last_vals = list()
total2 = 0

for history in lines:
    values = np.array(get_numbers(history))

    first_vals = list()

    while len(values.nonzero()[0]) != 0:
        last_vals.append(values[-1])
        first_vals.append(values[0])
        values = values[1:] - values[:-1]

    total2 += reduce(lambda x, y: y-x, first_vals[::-1])

total = sum(last_vals)

print("result part 1:", total)
print("result part 2:", total2)
