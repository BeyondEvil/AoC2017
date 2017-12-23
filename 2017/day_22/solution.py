from collections import defaultdict
from math import sqrt


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def turn(direction, heading):
    gps = {('up', 'right'): 'right',
           ('right', 'right'): 'down',
           ('down', 'right'): 'left',
           ('left', 'right'): 'up',
           ('up', 'left'): 'left',
           ('left', 'left'): 'down',
           ('down', 'left'): 'right',
           ('right', 'left'): 'up'}

    return gps.get((direction, heading))


def run_it(seq):

    grid = defaultdict(int)
    for r, row in enumerate(seq.split('\n')):
        for c, column in enumerate(row):
            grid[(r, c)] = 1 if column == '#' else 0

    start_row = start_column = int(sqrt(len(grid)) / 2)
    directions = {'right': (0, 1), 'down': (1, 0), 'left': (0, -1), 'up': (-1, 0)}

    bursts = 10000
    direction = 'up'
    row = start_row
    column = start_column
    infected = 0
    for _ in range(bursts):
        if grid.get((row, column), 0) == 1:  # infected, turn right
            grid[(row, column)] = 0  # cleaned
            direction = turn(direction, 'right')
        elif grid.get((row, column), 0) == 0:  # clean, turn left
            grid[(row, column)] = 1  # infected
            infected += 1
            direction = turn(direction, 'left')
        else:
            raise
        coord = directions.get(direction)
        row += coord[0]
        column += coord[1]

    print('Part 1: ', infected)


def turn2(state, direction):
    gps = {(0, 'up'): 'left',
           (0, 'right'): 'up',
           (0, 'left'): 'down',
           (0, 'down'): 'right',

           (1, 'up'): 'right',
           (1, 'right'): 'down',
           (1, 'left'): 'up',
           (1, 'down'): 'left',

           (2, 'up'): 'up',
           (2, 'right'): 'right',
           (2, 'left'): 'left',
           (2, 'down'): 'down',

           (3, 'up'): 'down',
           (3, 'right'): 'left',
           (3, 'left'): 'right',
           (3, 'down'): 'up'}

    return gps.get((state, direction))


def run_it2(seq):

    # clean: 0
    # infected: 1
    # weakened: 2
    # flagged: 3

    grid = defaultdict(int)
    for r, row in enumerate(seq.split('\n')):
        for c, column in enumerate(row):
            grid[(r, c)] = 1 if column == '#' else 0

    start_row = start_column = int(sqrt(len(grid)) / 2)
    directions = {'right': (0, 1), 'down': (1, 0), 'left': (0, -1), 'up': (-1, 0)}

    bursts = int(10e6)
    direction = 'up'
    row = start_row
    column = start_column
    infected = 0
    for _ in range(bursts):
        if grid.get((row, column), 0) == 1:  # infected
            grid[(row, column)] = 3  # flagged
            direction = turn2(1, direction)
        elif grid.get((row, column), 0) == 0:  # clean
            grid[(row, column)] = 2  # weakened
            direction = turn2(0, direction)
        elif grid.get((row, column), 0) == 2:  # weakened
            grid[(row, column)] = 1  # infected
            infected += 1
            direction = turn2(2, direction)
        elif grid.get((row, column), 0) == 3:  # flagged
            grid[(row, column)] = 0  # cleaned
            direction = turn2(3, direction)
        else:
            raise
        coord = directions.get(direction)
        row += coord[0]
        column += coord[1]

    print('Part 2: ', infected)


if __name__ == '__main__':

    run_it(read_input())  # 5399
    run_it2(read_input())
