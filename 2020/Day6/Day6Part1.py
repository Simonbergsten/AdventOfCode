import os
import sys
from _collections import  defaultdict
from collections import Counter
from typing import Callable, Iterable
from typing import Sequence, Mapping
testdata = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""

def get_input_data():
    with open(os.path.join(sys.path[0], "Input_data_day6"), "r") as f:
        input_data = f.readlines()
        # return data.split("\n\n")
        return input_data

def get_input_data_2():
    with open(os.path.join(sys.path[0], "Input_data_day6"), "r") as f:
        return f.read()


def solution_a():
    lines = get_input_data()
    total = 0
    letters = []

    for line in lines:
        if line == "\n":
            total += len(letters)
            letters = []
        else:
            line = line.rstrip()
            for c in line:
                if c not in letters:
                    letters.append(c)

    return total + len(letters)


# print(solution_a())



test = ["psyjxulrdtfejeusdrlxyftpufdpjsxrlztyeyeorabxsdnhftujlppedfxtsryujl"]
# print(len(set(test[0])))
PassportData = Mapping[str, str]
def read_data(data: str) -> Iterable[PassportData]:
    for block in data.split("\n\n"):
        yield dict(f.split(":", 1) for f in block.split())


newdata = get_input_data_2()
total = 0
# for block in newdata.rstrip().split("\n\n"):
#     unique_values = len(set(block))-1
#     # print(f"Unique values: {unique_values}")
#     total += unique_values

# print(f"Unique values: {total+1}")
# print(solution_a())


new_data = get_input_data_2()
total_score = 0
for block in new_data.split("\n\n"):
    counter = 1
    count_items = Counter(block.rstrip())
    del count_items["\n"]
    for line in block:
        print(line.rstrip())
        if line == "\n":
            counter += 1
    print(count_items)
    print("-----")
    print(counter)
    for value in count_items.values():
        if value == counter:
            total_score += 1

print(f"Total Score: {total_score}")

### Much cleaner solution

def solution_a(groups: Sequence[str]) -> int:
    return sum(len(set(group.replace("\n", ""))) for group in groups)

test = """\
abc

a
b
c

ab
ac

a
a
a
a

b
""".split("\n\n")

assert solution_a(test) == 11

def getData():
    with open("Input_data_day6", "r") as f:
        return f.read().split("\n\n")



data = getData()



print("Part 1: ", solution_a(data))

import aocd
