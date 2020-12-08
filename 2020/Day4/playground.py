from collections import Counter

string = "ezzmazaslfxnio"
string2 = "phmbaa"

counter = Counter(string)
print(counter)

for key, value in counter.items():
    print(key, value)

for value in counter.values():
    print(value)