"""
Expected Fields:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

Example of inputs:
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

import re
import os
import sys
import aocd
from marshmallow import fields, validate, RAISE, Schema, ValidationError
"""

"""

valid_keys = {'eyr': True, 'iyr': True, 'byr': True, 'ecl': True, 'pid': True,
              'hcl': True, 'hgt': True}


def get_input_data():
    with open(os.path.join(sys.path[0], "Day4_Input"), "r") as f:
        # return f.readlines()
        # return data.split("\n\n")
        return f.read()


def clean_data(input_data):
    "Replace \n with blank space"
    new_strings = []
    for string in input_data:
        new_string = string.replace("\n", " ")
        new_strings.append(new_string)
    return [line.split(" ") for line in new_strings]




def validation(passport):
    for items in passport:
        counter = 0
        for item in items:
            sep = item.split(":")
            # print(sep[0])
            counter
            if (sep[0] in valid_keys):
                counter += 1
                print("TRUE")

        print("\n")



#######
from typing import Callable, Iterable, Mapping
PassportData = Mapping[str, str]
Validator = Callable[[PassportData], bool]

required = frozenset({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"})
all_ = required | frozenset({"cid"})


def valid_passport(passport: PassportData) -> bool:
    return all_ >= passport.keys() >= required

def read_passports(data: str) -> Iterable[PassportData]:
    for block in data.split("\n\n"):
        yield dict(f.split(":", 1) for f in block.split())

def count_valid(passports: Iterable[PassportData], validator: Validator = valid_passport) -> int:
    return sum(1 for _ in filter(validator, passports))

testdata = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

assert count_valid(read_passports(testdata)) == 2
print(count_valid(read_passports(get_input_data())))

# export AOC_SESSION = 53616c7465645f5f7117cdccee97fa7879c4fc7608f8a4b3bc0c0b33d528f57ee29c8b7828e96d6dcf45d404b9aaa8be



### Validation of data
def validate_height(height: str) -> bool:
    try:
        value = int(height[:-2])
    except ValueError:
        raise ValidationError("Invalid height")

    if height[-2:] == "cm" and (150 <= value <= 193):
        return
    elif height[-2:] == "in" and (59 <= value <= 76):
        return
    raise ValidationError("Invalid height")


class PassportSchema(Schema):
    class Meta:
        unknown = 'RAISE'

    byr = fields.Int(required=True, validate=validate.Range(1920, 2002))
    iyr = fields.Int(required=True, validate=validate.Range(2010, 2020))
    eyr = fields.Int(required=True, validate=validate.Range(2020, 2030))
    hgt = fields.Str(required=True, validate=validate_height)
    hcl = fields.Str(required=True, validate=validate.Regexp(r"^#[0-9a-fA-F]{6}$"))
    ecl = fields.Str(
        required=True,
        validate=validate.OneOf(frozenset("amb blu brn gry grn hzl oth".split())),
    )
    pid = fields.Str(required=True, validate=validate.Regexp(r"^\d{9}$"))
    cid = fields.Str()


def valid_passport_fields(passport: Mapping):
    try:
        PassportSchema().load(passport)
        return True
    except ValidationError:
        return False


testinvalid = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

testvalid = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

assert count_valid(read_passports(testvalid), valid_passport_fields) == 4
assert count_valid(read_passports(testinvalid), valid_passport_fields) == 0

print("Part 2")
print(count_valid(read_passports(get_input_data()), valid_passport_fields))

