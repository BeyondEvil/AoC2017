import re
from collections import defaultdict


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):

    grid = defaultdict(bool)
    grid2 = defaultdict(int)
    for instruction in seq.splitlines():
        sx, sy, fx, fy = map(int, re.findall('\d+', instruction))
        for x in range(sx, fx + 1):
            for y in range(sy, fy + 1):
                if instruction.startswith('turn'):
                    grid[(x, y)] = 'on' in instruction
                    grid2[(x, y)] += 1 if 'on' in instruction else (-1 if grid2[(x, y)] else 0)
                else:
                    grid[(x, y)] = not grid[(x, y)]
                    grid2[(x, y)] += 2

    print('Part 1: ', sum(grid.values()))
    print('Part 2: ', sum(grid2.values()))


if __name__ == '__main__':

    run_it(read_input())  # 400410, 15343601
