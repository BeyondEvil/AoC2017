from collections import defaultdict


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def get(reg, v):
    try:
        return int(v)
    except ValueError:
        return int(reg[v])


def run_it(seq):
    instructions = seq.split('\n')
    registers = defaultdict(int)
    index = 0
    multi = 0
    while True:
        cmd = instructions[index].split()
        if cmd[0] == 'set':
            registers[cmd[1]] = get(registers, cmd[2])
        if cmd[0] == 'sub':
            registers[cmd[1]] -= get(registers, cmd[2])
        if cmd[0] == 'mul':
            registers[cmd[1]] *= get(registers, cmd[2])
            multi += 1
        if cmd[0] == 'jnz' and get(registers, cmd[1]) != 0:
            index += int(cmd[2])
        else:
            index += 1

        if index < 0 or index >= len(instructions):
            break

    print('Part 1: ', multi)


def run_it2():
    # https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/drngit2/
    # Run part 1 with register a set to 1, print registers and look for upper and lower bound.

    h = 0
    lower = 109300
    upper = 126300
    for x in range(lower, upper + 1, 17):
        for i in range(2, x):
            if x % i == 0:  # not prime, increment register h
                h += 1
                break

    print('Part 2: ', h)


if __name__ == '__main__':

    run_it(read_input())  # 8281
    run_it2()  # 911
