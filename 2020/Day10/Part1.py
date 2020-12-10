import os
import sys

def get_data():
    with open(os.path.join(sys.path[0], "Input_data_day10"), "r") as f:
        return [int(i) for i in f.readlines()]


def solve_a():
    data = get_data()
    data.sort()
    diff = dict({1:0, 2:0, 3:0})
    jolt = 0
    for i in data:
        d = i - jolt
        if d <= 3:
            diff[d] += 1
            jolt += d
    return diff[1] * (diff[3] + 1)


print(solve_a())


