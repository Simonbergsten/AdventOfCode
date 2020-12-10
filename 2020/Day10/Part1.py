import os
import sys

def get_data():
    with open(os.path.join(sys.path[0], "Input_data_day10"), "r") as f:
        return [int(i) for i in f.readlines()]


def solve_a():
    data = get_data()
    data.sort()
    diff = dict({1:0, 2:0, 3:0})
    jolt = 0
    for i in data:
        d = i - jolt
        if d <= 3:
            diff[d] += 1
            jolt += d
    return diff[1] * (diff[3] + 1)


# print(solve_a())

def solve_b():
    data_raw = open("Input_data_day10", "r")
    data = [int(line.strip()) for line in data_raw.readlines() if line.strip()]
    data.sort()
    data = [0] + data + [data[-1] + 3]
    last = 0
    a, b = 0, 0
    for x in data:
        assert x - last <= 3
        if x - last == 1:
            a += 1
        elif x - last == 3:
            b += 1
        last = x

    # print("part 1", a, b, a*b)

    dp = [1]
    for i in range(1, len(data)):
        ans = 0
        for j in range(i):
            if data[j] + 3 >= data[i]:
                ans += dp[j]

        dp.append(ans)

    return dp[-1]

print(solve_b())
