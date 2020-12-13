import os
import sys


def manhattan(a, b):
    # Manhattan length
    return sum([abs(a[x]-b[x]) for x in range(len(a))])


def getData():
    lines = []
    with open('Input_data_day12', 'r') as f:
        for line in f:
            lines.append(line.rstrip())

    return lines

def clean_data():
    clean_lines = []
    lines = getData()
    for line in lines:
        dir = line[0]
        stretch = line[1:]
        clean_lines.append([dir, int(stretch)])

    return clean_lines


def get_direction(current_direction, rotate):
    if rotate == 0:
        return current_direction

    if rotate < 0:
        return get_direction(current_direction, rotate + 4)

    if current_direction == [0, 1]:
        return get_direction([-1, 0], rotate - 1)

    if current_direction == [-1, 0]:
        return get_direction([0, -1], rotate-1)

    if current_direction == [0, -1]:
        return get_direction([1, 0], rotate-1)

    return get_direction([0, 1], rotate -1)


def solve_a():
    lines = clean_data()
    direction = [0, 1]
    y = 0
    x = 0

    for row in lines:
        command = row[0]
        magnitude = row[1]
        steps_to_rotate = magnitude // 90

        if command == "N":
            y += magnitude
        if command == "S":
            y -= magnitude
        if command == "E":
            x += magnitude
        if command == "W":
            x -= magnitude

        if command == "L":
            direction = get_direction(direction, -steps_to_rotate)
        if command == "R":
            direction = get_direction(direction, steps_to_rotate)

        if command == "F":
            y += magnitude * direction[0]
            x += magnitude * direction[1]


    return manhattan((y, x), (0, 0))


print(solve_a())