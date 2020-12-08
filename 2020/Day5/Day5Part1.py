import os
import sys
import math

def binary_search(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - 1) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid than it can only be present in the left subarray
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        # Else the the element can only be present in the right subarray
        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        # Element not present in the array
        return -1


#  arr = [2,3,4,10,40]
# x = 10
# print(binary_search(arr, 0, len(arr) - 1, x))


def get_data():
    with open(os.path.join(sys.path[0], "Input_data_day5"), "r") as f:
        return f.readlines()


data = get_data()


def seat_row(boarding_pass_first_part):
    max_row = 127
    min_row = 0
    idx = 1
    for element in boarding_pass_first_part:
        # print("Element is {}".format(element))
        if element == "B":
            min_row = ((max_row + min_row) // 2) + 1
            # print(f"Index: {idx} | Max row = {max_row} | Min row = {min_row}")
            idx += 1
        elif element == "F":
            max_row = (max_row + min_row) // 2
            # print(f"Index: {idx} | Max row = {max_row} | Min row = {min_row}")
            idx += 1

    assert max_row == min_row
    return max_row * 8


def seat_column(boarding_pass_second_part):
    max_col = 7
    min_col = 0
    for element in boarding_pass_second_part:
        if element == "R":
            min_col = ((max_col + min_col) // 2) + 1
        else:
            max_col = (max_col + min_col) // 2

    assert max_col == min_col
    return max_col


data_subset = data[0].rstrip()
data_first_part = data_subset[0:7]
data_second_part = data_subset[-3:]


# print(data_first_part)
# print(data_second_part)


def solve_a():
    data = get_data()
    scores = []
    for line in data:
        data_first_part = line.rstrip()[0:7]
        data_second_part = line.rstrip()[-3:]
        first_part_sum = seat_row(data_first_part)
        second_part_sum = seat_column(data_second_part)
        tot_sum = first_part_sum + second_part_sum
        scores.append(tot_sum)
    return max(scores), scores


max_score, scores = solve_a()
print(max_score)
# for line in data[0]:
#     newline = line.rstrip()
#     first_part = newline[0:6]
#     second_part = newline[-3:]
#     print("FIRST PART")
#     print(first_part)
#     print("\n")
#     max_row, min_row = seat_row(first_part)
#     print(f"Max row = {max_row} | Min row = {min_row}")


#### Part 2
from typing import Set
from itertools import tee, islice



def solve_b_2():
    data = get_data()
    possible_id = [i for i in range(1008)]
    for line in data:
        data_first_part = line.rstrip()[0:7]
        data_second_part = line.rstrip()[-3:]
        first_part_sum = seat_row(data_first_part)
        second_part_sum = seat_column(data_second_part)
        possible_id.remove(first_part_sum + second_part_sum)

    return possible_id




def get_row(row):
    upper = 127
    lower = 0

    for c in row:
        if c == "F":
            upper -= math.ceil((upper - lower) / 2)
        else:
            lower += math.ceil((upper - lower) / 2)

    return upper


def get_col(col):
    upper = 7
    lower = 0
    for c in col:
        if c == "L":
            upper -= math.ceil((upper - lower) / 2)
        else:
            lower += math.ceil((upper - lower) / 2)

    return upper


def get_seat_id(line):
    return (get_row(line[:-3]) * 8) + get_col(line[7:])


def solve_a_2():
    lines = get_data()
    highest = 0
    for line in lines:
        sid = get_seat_id(line)
        highest = sid if sid > highest else highest

    return highest

print(solve_a_2())

def solve_b():
    emptyseats = []
    max_val, values = solve_a()
    possible_id = [i for i in range(1, max_val + 1)]
    for check in range(1, max_val + 1):
        if check not in values:
            emptyseats.append(check)
    for seat in range(10, max_val+1-8):
        if (seat - 1 not in emptyseats and seat in emptyseats and seat + 1 not in emptyseats):
            print(seat)

    # lines = get_data()
    # for line in lines:
    #     possible_id.remove(get_seat_id(line))

    # return possible_id

solve_b()

