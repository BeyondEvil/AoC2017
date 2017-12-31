import re
from collections import defaultdict


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):

    grid = defaultdict(int)
    for instruction in seq.splitlines():
        sx, sy, fx, fy = map(int, re.findall('\d+', instruction))
        if instruction.startswith('turn on'):
            for x in range(sx, fx + 1):
                for y in range(sy, fy + 1):
                    grid[(x, y)] = 1

        elif instruction.startswith('turn off'):
            for x in range(sx, fx + 1):
                for y in range(sy, fy + 1):
                    grid[(x, y)] = 0

        else:  # toggle
            for x in range(sx, fx + 1):
                for y in range(sy, fy + 1):
                    grid[(x, y)] = 0 if grid[(x, y)] else 1

    print('Part 1: ', sum(grid.values()))

    grid = defaultdict(int)
    for instruction in seq.splitlines():
        sx, sy, fx, fy = map(int, re.findall('\d+', instruction))
        if instruction.startswith('turn on'):
            for x in range(sx, fx + 1):
                for y in range(sy, fy + 1):
                    grid[(x, y)] += 1

        elif instruction.startswith('turn off'):
            for x in range(sx, fx + 1):
                for y in range(sy, fy + 1):
                    if grid[(x, y)]:
                        grid[(x, y)] -= 1

        else:  # toggle
            for x in range(sx, fx + 1):
                for y in range(sy, fy + 1):
                    grid[(x, y)] += 2

    print('Part 2: ', sum(grid.values()))


if __name__ == '__main__':

    run_it(read_input())  # 400410, 15343601
