import os
import sys
import random
import itertools


def get_data():
    with open(os.path.join(sys.path[0], "Input_data_day9"), "r") as f:
        return [int(i) for i in f.readlines()]

# print(len(get_data()[0:25]))

for item in get_data()[0:25]:
    print(item)

def findTarget(nums, target):
    required = {}

    for i in range(len(nums)):
        if target - nums[i] in required:
            return True
            # return [required[target- nums[i]], i]
        else:
            required[nums[i]] = i

    return False


def solve_a():
    data = get_data()
    sub_length = 25
    prev = data[:sub_length]
    data = data[sub_length:]

    for n in data:
        if not match(prev, n):
            return n
        prev.append(n)
        prev.pop(0)

    return None


def match(nums, target):
    for n in nums:
        if (target - n) in nums and n != (target - n):
            return True
    return False


def batch(iterable, n=1):
    l = len(iterable)
    print(l)
    start = 0
    for ndx in range(start, l, n):
        yield iterable[start:start + n]
        start += 1


print(solve_a())
