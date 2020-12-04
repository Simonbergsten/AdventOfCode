import re
import os
import sys

with open(os.path.join(sys.path[0], "passwords"), "r") as f:
    content = [line.rstrip() for line in f]


#def isValidPasword(string):
#     pattern = re.compile("[0-9]+-[0-9]+\s([a-z]):\s[a-z]+")
#     if re.match(pattern, string):
#         return True
#     else:
#         return False


def split_string(string):
    arr = string.split(" ")
    length_str = arr[0].split("-")
    length_str = [int(i) for i in length_str]
    character = arr[1][0]
    password = arr[2].strip()
    dict = {}
    dict["character"] = character
    dict["min_length"] = length_str[0]
    dict["max_length"] = length_str[1]
    dict["password"] = password
    return dict



def val_password(string):
    num_of_valids = 0
    # is_valid = isValidPasword(string)
    # if is_valid:
    for item in string:
        clean_data = split_string(item)
        max_length = clean_data['max_length']
        min_length = clean_data['min_length']
        password = clean_data['password']
        character = clean_data['character']

        if password.count(character) >= min_length and password.count(character) <= max_length:
            num_of_valids += 1

    return num_of_valids

print(val_password(content))
