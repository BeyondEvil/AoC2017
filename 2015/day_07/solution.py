import re
import operator
from collections import defaultdict


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def get(parts, v):
    try:
        return int(v)
    except ValueError:
        v = parts[v]
        if v is not None:
            return v


def run_it(seq):
    operation = {'AND': operator.and_,
                 'LSHIFT': operator.lshift,
                 'RSHIFT': operator.rshift,
                 'OR': operator.or_}

    std_gates = ['AND', 'OR', 'RSHIFT', 'LSHIFT']

    pattern = '(?:(?:(?:(\S+) )?(.*)) )?(\S+) -> (\S+)'

    wires = defaultdict(lambda: None)
    while not wires['a']:
        for instruction in seq.splitlines():
            a, op, b, out = re.findall(pattern, instruction)[0]
            a = get(wires, a)
            b = get(wires, b)

            if op == 'NOT':
                if b is not None:
                    wires[out] = ~b
            elif op == '':  # assign
                if b is not None:
                    wires[out] = b
            elif op in std_gates:
                if a is not None and b is not None:
                    wires[out] = operation[op](a, b)
            else:
                assert False

    part_one = wires['a']

    wires = defaultdict(lambda: None)  # lazy reset
    wires['b'] = part_one
    while not wires['a']:
        for instruction in seq.splitlines():
            a, op, b, out = re.findall(pattern, instruction)[0]
            a = get(wires, a)
            b = get(wires, b)

            # overriding wire b with wire a by basically
            # skipping to write anything new to it
            if out == 'b':
                continue

            if op == 'NOT':
                if b is not None:
                    wires[out] = ~b
            elif op == '':  # assign
                if b is not None:
                    wires[out] = b
            elif op in std_gates:
                if a is not None and b is not None:
                    wires[out] = operation[op](a, b)
            else:
                assert False

    print('Part 1: ', part_one)
    print('Part 2: ', wires['a'])


if __name__ == '__main__':

    run_it(read_input())  # 3176, 14710
