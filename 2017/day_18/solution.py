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
    last_freq = 0
    registers = defaultdict(int)
    index = 0
    while True:
        cmd = instructions[index].split()
        if cmd[0] == 'snd':
            last_freq = registers[cmd[1]]
        if cmd[0] == 'set':
            registers[cmd[1]] = get(registers, cmd[2])
        if cmd[0] == 'add':
            registers[cmd[1]] += get(registers, cmd[2])
        if cmd[0] == 'mul':
            registers[cmd[1]] *= get(registers, cmd[2])
        if cmd[0] == 'mod':
            registers[cmd[1]] %= get(registers, cmd[2])
        if cmd[0] == 'rcv' and registers[cmd[1]] != 0:
            registers[cmd[1]] = last_freq
            break
        if cmd[0] == 'jgz'and registers[cmd[1]] > 0:
            index += get(registers, cmd[2])
        else:
            index += 1

        if index < 0 or index > len(instructions):
            break

    print('Part 1: ', last_freq)


queue = [[], []]


def run(seq, program):
    instructions = seq.split('\n')
    registers = defaultdict(int)
    registers['p'] = program
    sender = program
    receiver = 1 - program
    index = 0
    sends = 0
    while True:
        try:
            cmd = instructions[index].split()
            if cmd[0] == 'snd':
                queue[receiver].append(get(registers, cmd[1]))
                sends += 1
                yield sends
            if cmd[0] == 'set':
                registers[cmd[1]] = get(registers, cmd[2])
            if cmd[0] == 'add':
                registers[cmd[1]] += get(registers, cmd[2])
            if cmd[0] == 'mul':
                registers[cmd[1]] *= get(registers, cmd[2])
            if cmd[0] == 'mod':
                registers[cmd[1]] %= get(registers, cmd[2])
            if cmd[0] == 'rcv':
                registers[cmd[1]] = queue[sender].pop(0)
                yield sends

            if cmd[0] == 'jgz' and get(registers, cmd[1]) > 0:
                index += get(registers, cmd[2])
            else:
                index += 1
        except:
            return


def run_it_part2(seq):
    p_zero = run(seq, 0)
    p_one = run(seq, 1)
    value = None
    while True:
        try:
            next(p_zero)
            value = next(p_one)
        except StopIteration:
            break

    print('Part 2: ', value)


if __name__ == '__main__':

    _seq = read_input()
    run_it(_seq)  # 1187
    run_it_part2(_seq)  # 5969
