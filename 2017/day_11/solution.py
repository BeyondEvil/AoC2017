
def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    directions = {'n': (0, -1),
                  'ne': (1, -1),
                  'se': (1, 0),
                  's': (0, 1),
                  'sw': (-1, 1),
                  'nw': (-1, 0)}
    x = 0
    y = 0
    distances = []
    for direction in seq.split(','):
        _x, _y = directions.get(direction)
        x += _x
        y += _y
        z = 0 - x - y
        distance = max(abs(0 - x), abs(0 - y), abs(0 - z))
        distances.append(distance)

    print('Part 1: ', distances[-1])
    print('Part 2: ', max(distances))


if __name__ == '__main__':
    # https://www.redblobgames.com/grids/hexagons/
    run_it(read_input())  # 722, 1551
