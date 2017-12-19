

def read_input():
    with open('input.txt', 'r') as f:
        return f.read()


def run_it(seq):
    grid = seq.splitlines(True)
    start = grid[0].find('|')

    node_lookup = {(0, start): '|'}
    for ir, row in enumerate(grid[1:]):
        for ic, column in enumerate(row):
            if column.strip():
                node_lookup.update({(ir + 1, ic): column})

    seen = set()
    seen.add((0, start))
    next_direction = 'down'
    x = 1
    y = start
    next_coord = (x, y)
    letters = ''
    steps = 1
    while True:
        seen.add(next_coord)
        direction = node_lookup.get(next_coord)

        if direction is None:
            break

        if direction.isalpha():
            letters += direction
            if next_direction == 'down':
                x += 1
            if next_direction == 'up':
                x -= 1
            if next_direction == 'right':
                y += 1
            if next_direction == 'left':
                y -= 1
            next_coord = (x, y)

        elif direction == '+':
            coords = {(0, 1): 'right', (1, 0): 'down', (0, -1): 'left', (-1, 0): 'up'}
            for coord in coords.keys():
                row = x + coord[0]
                column = y + coord[1]
                next_node = node_lookup.get((row, column))
                if next_node and (row, column) not in seen:
                    next_direction = coords.get(coord)
                    next_coord = (row, column)
                    x = row
                    y = column

        else:  # intersection
            if next_direction == 'down':
                x += 1
            if next_direction == 'up':
                x -= 1
            if next_direction == 'right':
                y += 1
            if next_direction == 'left':
                y -= 1
            next_coord = (x, y)

        steps += 1

    print('Part 1: ', letters)
    print('Part 2: ', steps)


if __name__ == '__main__':

    run_it(read_input())  # KGPTMEJVS, 16328
