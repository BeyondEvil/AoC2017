import re
import operator as op
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
    operation = {'AND': op.and_,
                 'LSHIFT': op.lshift,
                 'RSHIFT': op.rshift,
                 'OR': op.or_}

    wires = defaultdict(int)
    while not wires['a']:
        for instruction in seq.splitlines():
            cmd = re.split(' | -> ', instruction)
            cmd.remove('->')
            if len(cmd) == 2:  # 123 -> x
                v, w = cmd
                v = get(wires, v)
                if v:
                    wires[w] = v
            elif len(cmd) == 3:  # NOT x -> h
                _, v, w = cmd
                if v:
                    v = get(wires, v)
                    wires[w] = v
            elif len(cmd) == 4:  # x AND y -> d
                v1, o, v2, w = cmd
                v1 = get(wires, v1)
                v2 = get(wires, v2)
                if v1 and v2:
                    wires[w] = operation[o](v1, v2)
            else:
                assert False

    print('Part 1: ', wires['a'])
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it("""x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
123 -> x
456 -> y""")  #

    #run_it(read_input())
