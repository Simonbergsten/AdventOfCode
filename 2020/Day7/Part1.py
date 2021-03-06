import re
import os
import sys
"""

"""
checked_a = {"shiny gold":True, 'other':False}
checked_b = {'other': 0}


def get_input_data():
    with open(os.path.join(sys.path[0], "input_data_day7"), "r") as f:
        numbers = f.readlines()
        return numbers

# data = get_input_data()
# for line in data:
#     print(line.strip())


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


def find_nr_of_bags(bag, outer, inner):

    if bag in checked_b:
        return checked_b.get(bag)

    nr = 1
    i = outer.index(bag)

    for bags in inner[i]:
        if bags[0].isnumeric():
            nr += int(bags[0]) * find_nr_of_bags(bags[1], outer, inner)
        else:
            nr += find_nr_of_bags(bags[1], outer, inner)

    checked_b[bag] = nr
    return nr


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

def solve_b():
    outer, inner = get_rules()
    return find_nr_of_bags("shiny gold", outer, inner) - 1

print(solve_a())
print(solve_b())



