from collections import defaultdict


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    coord = {'^': (0, 1),
             'v': (0, -1),
             '>': (1, 0),
             '<': (-1, 0)}

    houses = defaultdict(int)
    x, y = (0, 0)
    for direction in seq:
        houses[(x, y)] = True
        dx, dy = coord[direction]
        x += dx
        y += dy

    print('Part 1: ', sum(houses.values()))

    santa_houses = defaultdict(int)
    robo_houses = defaultdict(int)
    sx, sy = rx, ry = (0, 0)
    santa_houses[(sx, sy)] = True
    robo_houses[(rx, ry)] = True
    coords = {True: [(0, 0), santa_houses], False: [(0, 0), robo_houses]}
    santa = True
    for direction in seq:
        dx, dy = coord[direction]
        x, y = coords[santa][0]
        x += dx
        y += dy
        coords[santa][0] = (x, y)
        coords[santa][1][(x, y)] = True
        santa = not santa

    santa_houses.update(robo_houses)

    print('Part 2: ', sum(santa_houses.values()))


if __name__ == '__main__':

    run_it(read_input())  # 2081, 2341
