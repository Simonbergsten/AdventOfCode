import os
import sys

def get_data():
    with open(os.path.join(sys.path[0], "Input_data_day8"), "r") as f:
        return f.readlines()

data = get_data()


# for line in data[0:10]:
#     splitted = line.rstrip().split(" ")
#     first_part = splitted[0]
#     second_part = int(splitted[1])

idx = 0
accumulator = 0
dict = {}
new_data = [i.rstrip().split(" ") for i in data]
while idx not in dict:
    dict[idx] = True
    element = new_data[idx]
    if element[0].rstrip() == 'jmp':
        idx += int(element[1].rstrip())-1
    if element[0].rstrip() == "acc":
        idx += 1
        accumulator += int(element[1].rstrip())
    else:
        idx += 1

print(accumulator)
