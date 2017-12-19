

def read_input():
    with open('input.txt', 'r') as f:
        return f.read()


def run_it(seq):
    grid = seq.splitlines(True)
    node_lookup = {}
    x = y = None
    for ir, row in enumerate(grid):
        for ic, column in enumerate(row):
            if column.strip():
                if not any([x, y]):
                    x = ir
                    y = ic
                node_lookup.update({(ir, ic): column})

    coords = {(0, 1): 'right', (1, 0): 'down', (0, -1): 'left', (-1, 0): 'up'}
    seen = list()
    next_direction = 'down'
    path = []
    while True:
        next_coord = (x, y)
        seen.append(next_coord)
        direction = node_lookup.get(next_coord)

        if direction is None:
            break

        path.append(direction)
        if direction == '+':
            for coord in coords.keys():
                row = x + coord[0]
                column = y + coord[1]
                next_node = node_lookup.get((row, column))
                if next_node and (row, column) not in seen:
                    next_direction = coords.get(coord)
                    x = row
                    y = column

        else:
            if next_direction == 'down':
                x += 1
            if next_direction == 'up':
                x -= 1
            if next_direction == 'right':
                y += 1
            if next_direction == 'left':
                y -= 1

    print('Part 1: ', ''.join([p for p in path if p.isalpha()]))
    print('Part 2: ', len(path))


if __name__ == '__main__':

    run_it(read_input())  # KGPTMEJVS, 16328
