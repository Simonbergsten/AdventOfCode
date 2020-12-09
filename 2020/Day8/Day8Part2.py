import os
import sys

programl = []

def get_data():
    with open(os.path.join(sys.path[0], "Input_data_day8"), "r") as f:
        return f.readlines()

def clean_data():
    lines = get_data()
    for line in lines:
        instruction, nr = line.strip().split()
        programl.append((instruction, int(nr)))
    programl.append(("end", 0))


clean_data()
# tempprog = []
# for line in programl:
#     tempprog.append(list(line))
#
# print(tempprog)

def run_program(program):
    accumulator = 0
    checked = []
    pc = 0
    finished = False

    while pc not in checked:
        pline = program[pc]
        checked.append(pc)

        if pline[0] == "nop":
            pc += 1
        elif pline[0] == "acc":
            accumulator += pline[1]
            pc += 1
        elif pline[0] == "jmp":
            pc += pline[1]
        else:
            finished = True

    return accumulator, finished


def make_tempprog():
    tempprog = []
    for line in programl:
        tempprog.append(list(line))
    return tempprog


def solve_a():
    return run_program(programl)



# print(solve_a())

def solve_b():
    f_acc = None
    for i, line in enumerate(programl):
        if line[0] == "acc":
            continue

        temp = make_tempprog()
        if line[0] == "nop":
            temp[i][0] = "jmp"

        elif line[0] == 'jmp':
            temp[i][0] = 'nop'

        acc, fin = run_program(temp)
        if fin is True:
            f_acc = acc

    return f_acc


print(solve_b())

tempprogram = make_tempprog()
print(tempprogram)


