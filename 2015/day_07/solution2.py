import re
from collections import defaultdict


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def get(parts, v):
    try:
        return int(v)
    except ValueError:
        return int(parts[v])


def run_it(seq):

    wires = defaultdict(int)
    while not wires['a']:
        print wires
        for instruction in seq.splitlines():
            match = re.findall('(?:(?:(\S+) )?(.*)) (\S+) -> (\S+)', instruction)
            if match:
                a, op, b, out = match[0]
                a = get(wires, a)
                b = get(wires, a)
            else:
                match = re.findall('(\d+) -> (\S+)', instruction)
                if match:
                    v, out = match[0]
                else:
                    v, out = re.findall('(\S+) -> (\S+)', instruction)[0]
                v = get(wires, v)

            if op == 'AND':
                if not (a and b):
                    continue
                wires[out] = a & b
            elif op == 'OR':
                if not (a and b):
                    continue
                wires[out] = a | b
            elif op == 'NOT':
                if not b:
                    continue
                wires[out] = ~b
            elif op == 'RSHIFT':
                if not (a and b):
                    continue
                wires[out] = a >> b
            elif op == 'LSHIFT':
                if not (a and b):
                    continue
                wires[out] = a << b
            else:  # assign
                if not v:
                    continue
                wires[out] = v

    print('Part 1: ', wires['a'])
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it(read_input())
