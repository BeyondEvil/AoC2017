def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def build_matrix(square, sums=None):
    from itertools import cycle

    directions = cycle(['right', 'up', 'left', 'down'])

    print("Init matrix...")
    matrix = {}
    for value in range(square):
        matrix[value + 1] = {'x': None, 'y': None}

    print("Done.\n\nStart building...")

    start = 2
    end = square
    x = 0
    y = 0
    matrix[1] = {'x': 0, 'y': 0}
    next_direction = next(directions)
    template = "({},{})"
    seen = [template.format(x, y)]
    while start <= end:
        if next_direction == 'right':
            x += 1
            if template.format(x, (y + 1)) not in seen:
                next_direction = next(directions)

        elif next_direction == 'up':
            y += 1
            if template.format((x - 1), y) not in seen:
                next_direction = next(directions)

        elif next_direction == 'left':
            x -= 1
            if template.format(x, (y - 1)) not in seen:
                next_direction = next(directions)

        elif next_direction == 'down':
            y -= 1
            if template.format((x + 1), y) not in seen:
                next_direction = next(directions)

        matrix[start] = {'x': x, 'y': y}
        total_sum = get_sum(x, y, sums)
        if sums and total_sum > square:
            return total_sum
        seen.append(template.format(x, y))
        start += 1

    print ("Done.")
    return matrix


def get_sum(x, y, sums):
    neighbours = [(x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1),
                  (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    _sum = 0
    for each in neighbours:
        _sum += sums.get(each, 0)

    sums[(x, y)] = _sum
    return _sum


def run_it(seq):
    seq = int(seq)
    matrix = build_matrix(seq)
    coords = matrix.get(seq)

    print('Part 1: ', abs(coords['x']) + abs(coords['y']))
    print('Part 2: ', build_matrix(seq, {(0, 0): 1}))


if __name__ == '__main__':

    run_it(read_input())  # 430, 312453
