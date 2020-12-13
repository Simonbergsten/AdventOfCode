import os
import sys
from collections import Counter
from functools import lru_cache
import heapq
import itertools
import math
import random

# from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, neighs, neighs_bounded


"""
Rule 1: If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
Rule 2: If a seat is occupield (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
"""


def getData():
    lines = []
    with open("Input_data_day11", "r") as f:
        for line in f.readlines():
            lines.append(line.rstrip())

    return lines


def solve(data):
    height = len(data)
    width = len(data[0])

    while True:
        changed = False

        newdata = [list(line) for line in data]

        for y in range(height):
            for x in range(width):
                c = data[y][x]

                if c == ".":
                    continue

                occupied = 0

                for dy, dx in eight_neighs_bounded(y, x, 0, height - 1, 0, width - 1):
                    if data[dy][dx] == "#":
                        occupied += 1

                if c == "L" and occupied == 0:
                    newdata[y][x] = "#"
                    changed = True
                if c == "#" and occupied >= 4:
                    newdata[y][x] = "L"
                    changed = True

        if not changed:
            break

        data = newdata

    return sum(sum(c == "#" for c in row) for row in data)


def eight_neighs_bounded(y, x, rmin, rmax, cmin, cmax):
    neighs = []

    up = y > rmin
    down = y < rmax
    left = x > cmin
    right = x < cmax

    if up:
        neighs.append([y - 1, x])
        if left:
            neighs.append([y - 1, x - 1])
        if right:
            neighs.append([y - 1, x + 1])
    if down:
        neighs.append([y + 1, x])
        if left:
            neighs.append([y + 1, x - 1])
        if right:
            neighs.append([y + 1, x + 1])
    if left:
        neighs.append([y, x - 1])
    if right:
        neighs.append([y, x + 1])

    return neighs

data = getData()
print(solve(data))


def solve_b():
    data = getData()


data = getData()
for line in data:
    print(line)
