"""
In this task, we are supposed to add 3 numbers instead of two and then multiply them
"""
import os
import sys

with open(os.path.join(sys.path[0], "numbers"), "r") as f:
    content = [int(line.rstrip()) for line in f]


def find_target_3_sum(array, target):
    for i in range(len(array) - 1):
        s = set()
        currentSum = target - array[i]
        for j in range(i+1 ,len(array)):
            if (currentSum  - array[j]) in s:
                assert array[i] + array[j] + (currentSum - array[j]) == target
                print("Multiplication gives: {}".format(array[i] * array[j] * (currentSum - array[j])))
                return [array[i], array[j], currentSum - array[j]]
            s.add(array[j])
    return -1

print(find_target_3_sum(content, 2020))
