
def getData():
    lines = []
    with open("Data_day_15", "r") as f:
        for line in f.readlines():
            lines.append(line)

    return [int(x) for x in lines[0].split(",")]


def solve_a():
    inp = getData()
    n = 0
    nums = {}
    last = 0
    for i in range(len(inp)):
        n += 1
        nums[inp[i]] = [n]
        last = inp[i]

    while n != 2020:
        n += 1
        if len(nums[last]) == 1:
            new = 0
        else:
            new = nums[last][-1] - nums[last][-2]
        if new in nums:
            nums[new].append(n)
        else:
            nums[new] = [n]

        last = new

    return last


print(solve_a())


def solve_b():
    inp = getData()
    n = 0
    nums = {}
    last = 0
    for i in range(len(inp)):
        n += 1
        nums[inp[i]] = [n]
        last = inp[i]

    while n != 30000000:
        n += 1
        if len(nums[last]) == 1:
            new = 0
        else:
            new = nums[last][-1] - nums[last][-2]
        if new in nums:
            nums[new].append(n)
        else:
            nums[new] = [n]

        last = new

    return last

print(solve_b())