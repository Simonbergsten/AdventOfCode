import re
import os
import sys
"""

"""

with open(os.path.join(sys.path[0], "passwords"), "r") as f:
    content = [line.rstrip() for line in f]


def split_string(string):
    arr = string.split(" ")
    length_str = arr[0].split("-")
    length_str = [int(i) for i in length_str]
    character = arr[1][0]
    password = arr[2].strip()
    dict = {}
    dict["character"] = character
    dict["first_index"] = length_str[0]
    dict["second_index"] = length_str[1]
    dict["password"] = password
    return dict


def validate_string(string):
    sum_valid = 0
    for idx in string:
        clean_data = split_string(idx)
        first_index = clean_data['first_index']
        second_index = clean_data['second_index']
        password = clean_data['password']
        character = clean_data['character']

        if (password[first_index-1] == character and password[second_index-1] != character) or \
                (password[first_index-1] != character and password[second_index-1] == character):
            sum_valid += 1

    return sum_valid

print(validate_string(content))