""""
For example, suppose your expense report contained the following:
1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579,
so the correct answer is 514579.


"""
import os
import sys

with open(os.path.join(sys.path[0], "numbers"), "r") as f:
    content = [int(line.rstrip()) for line in f]

def sums_to_target(nums ,target):
    required = {}
    for i in range(len(nums)):
        if target  - nums[i] in required:
            return [target - nums[i], nums[i]]
            # return [required[target - nums[i]], i]
        else:
            required[nums[i]] = i
    return -1

answer = sums_to_target(content, 2020)
assert answer[0] + answer[1] == 2020

print(sums_to_target(content, 2020))
# Then multiply
print("Multiplying both number: ")
print("= {} * {} = {}".format(answer[0], answer[1], answer[0] * answer[1]))


