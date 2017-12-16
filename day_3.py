def run_it_a(square):
    matrix = build_matrix(square)
    coords = matrix.get(square)
    distance = abs(coords['x'] + coords['y'])
    print distance
    distance = abs(0 - coords['x']) + abs(0 - coords['y'])
    print distance
    return distance


def build_matrix(square):
    from itertools import cycle

    directions = cycle(['right', 'up', 'left', 'down'])

    print "Init matrix..."
    matrix = {}
    for value in range(square):
        matrix[value + 1] = {'x': None, 'y': None}

    print "Done.\n\nStart building..."

    start = 2
    end = square
    x = 0
    y = 0
    matrix[1] = {'x': 0, 'y': 0}
    next_direction = directions.next()
    template = "({},{})"
    seen = [template.format(x, y)]
    while start <= end:
        if next_direction == 'right':
            x += 1
            if template.format(x, (y + 1)) not in seen:
                next_direction = directions.next()

        elif next_direction == 'up':
            y += 1
            if template.format((x - 1), y) not in seen:
                next_direction = directions.next()

        elif next_direction == 'left':
            x -= 1
            if template.format(x, (y - 1)) not in seen:
                next_direction = directions.next()

        elif next_direction == 'down':
            y -= 1
            if template.format((x + 1), y) not in seen:
                next_direction = directions.next()

        matrix[start] = {'x': x, 'y': y}
        seen.append(template.format(x, y))
        start += 1
        print "Value: ", start
    print "Done."
    return matrix


"""n = (x, y)
        1 = (0, 0)
        2 = (1, 0)
        3 = (1, 1)
        4 = (0, 1)
        5 = (-1, 1)
        6 = (-1, 0)
        7 = (-1, -1)
        8 = (0, -1)
        9 = (1, -1)
        10 = (2, -1)
        11 = (2, 0)
        12 = (2, 1)
        ...
        23 = (0, -2)"""


def run_it_b(square):
    matrix = build_matrix2(square)
    return 0


def build_matrix2(square):
    from itertools import cycle

    directions = cycle(['right', 'up', 'left', 'down'])

    print "Init matrix..."
    matrix = {}
    for value in range(square):
        matrix[value + 1] = {'x': None, 'y': None}

    print "Done.\n\nStart building..."

    start = 2
    end = square
    x = 0
    y = 0
    matrix[1] = {'x': 0, 'y': 0}
    next_direction = directions.next()
    template = "({},{})"
    seen = [template.format(x, y)]
    sums = {(0, 0): 1}
    while start <= end:
        if next_direction == 'right':
            x += 1
            if template.format(x, (y + 1)) not in seen:
                next_direction = directions.next()

        elif next_direction == 'up':
            y += 1
            if template.format((x - 1), y) not in seen:
                next_direction = directions.next()

        elif next_direction == 'left':
            x -= 1
            if template.format(x, (y - 1)) not in seen:
                next_direction = directions.next()

        elif next_direction == 'down':
            y -= 1
            if template.format((x + 1), y) not in seen:
                next_direction = directions.next()

        matrix[start] = {'x': x, 'y': y}
        _sum = get_sum(x, y, sums)
        if _sum > square:
            print "SUM: ", _sum
            break
        seen.append(template.format(x, y))
        start += 1
    print "Done."
    return matrix


def get_sum(x, y, sums):
    neighbours = [(x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1),
                  (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    _sum = 0
    for each in neighbours:
        _sum += sums.get(each, 0)

    sums[(x, y)] = _sum
    return _sum


if __name__ == '__main__':
    #run_it_a(312051)

    run_it_b(312051)
