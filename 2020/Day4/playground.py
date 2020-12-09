# from collections import Counter
#
# string = "ezzmazaslfxnio"
# string2 = "phmbaa"
#
# counter = Counter(string)
# print(counter)
#
# for key, value in counter.items():
#     print(key, value)
#
# for value in counter.values():
#     print(value)
#
# dict = {'x': True, 'y': True}
# print("z" in dict)
#
# math = '-3'
# math_int = int(math)
# print(math_int * 3)

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

new_data = [["nop", "+0"], ["acc", "+1"], ["jmp", "+4"], ["acc", "+3"], ["jmp", "-3"], ["acc", "-99"],
             ["acc", "+1"], ["jmp", "-4"], ["acc", "+6"]]

idx = 0
accumulator = 0
dict = {}
while idx not in dict:
    print(idx)
    dict[idx] = True
    element = new_data[idx]
    if element[0].rstrip() == 'jmp':
        idx += int(element[1].rstrip())-1
    if element[0].rstrip() == "acc":
        idx += 1
        accumulator += int(element[1].rstrip())
    else:
        idx += 1

print(f"Accumulated sum: {accumulator}")