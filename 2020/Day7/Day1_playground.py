import re
import os
import sys
"""

"""
checked_a = {"shiny gold":True, 'other':False}
checked_b = {'other':0}


def get_input_data():
    with open(os.path.join(sys.path[0], "input_data_day7"), "r") as f:
        numbers = f.readlines()
        return numbers



def get_rules():
    lines = get_input_data()

    outer_bags = []
    inner_bags = []

    for line in lines:
        sline = line.rstrip()
        outer, inner = sline.split("contain")
        outer_bags.append(outer[:-6])

        innerbags = inner.split(",")
        inside = []

        for cont in innerbags:
            shaved = cont[:-1] if cont[-1] == "." else cont

            intuple = (shaved[:2].strip(), shaved.strip()[2:-4].strip())
            inside.append(intuple)

        inner_bags.append(inside)

    return outer_bags, inner_bags

def solve_a():
    outer, inner = get_rules()
    found = 0
    for bag in outer:
        if find_shiny_gold(bag, outer, inner):
            found += 1
    return found - 1

def find_shiny_gold(bag, outer, inner):
    if bag in checked_a:
        return checked_a.get(bag)

    i = outer.index(bag)
    for bags in inner[i]:
        if find_shiny_gold(bags[1], outer, inner) is True:
            checked_a[bag] = True
            return True

    checked_a[bag] = False
    return False




# print("Outer")
# print(outer)
# print("inner")
# print(inner)
# data = get_input_data()
outer, inner = get_rules()
print(outer)
print(inner)
for bag in outer[0:3]:
    print(bag)

print(outer[0:2])
print(outer[0])
# print(find_shiny_gold(outer[0],outer[0:2], inner[0:2]))
test = outer[267]
print(outer.index(test))
print("TEST")
if test in checked_a:
    print(checked_a.get(test))

print("\n")
print("\n")
print(outer[0:2])
print(outer[0])
print(inner[0:2])
print("TEST")
print(outer[1])
print(inner[1])