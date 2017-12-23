from collections import deque
from itertools import izip_longest
from functools import reduce
from operator import xor


class Node(object):

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        self.neighbours = []

    def find_neighbours(self, grid):
        if self.data:
            for coord in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                try:
                    x = self.x + coord[0]
                    y = self.y + coord[1]
                    if x >= 0 and y >= 0:
                        node = grid[x][y]
                        if node.data:
                            self.neighbours.append(node)
                except IndexError:
                    continue

    def get_region(self, region=None):
        if not region:
            region = [self] if self.data else []

        if self.data:
            for neigh in self.neighbours:
                if neigh not in region:
                    region.append(neigh)
                    neigh.get_region(region)
        return region


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def reverse_sublist(lst, start, end):
    sublist = lst[start:end]
    sublist.reverse()
    lst[start:end] = sublist


def run(_input):
    input_lengths = [ord(i) for i in _input]
    input_lengths.extend([17, 31, 73, 47, 23])
    circular_list = deque(range(256))

    rounds = 64
    rotation = 0
    skip = 0
    for index in range(rounds):
        for length in input_lengths:
            circular_list.rotate(rotation * -1)
            tmp_list = list(circular_list)
            reverse_sublist(tmp_list, 0, length)
            circular_list = deque(tmp_list)
            circular_list.rotate(rotation)
            rotation += length + skip
            skip += 1

    block_size = 16
    dense_hash = []
    for chunk in grouper(circular_list, block_size):
        dense_hash.append(reduce(xor, chunk))

    return ''.join(map('{:02x}'.format, dense_hash))


def run_it(seq):
    rows = 128
    row_sums = []
    nodes = []
    grid = [[0]*rows for _ in range(rows)]
    for row in range(rows):
        v = run(seq+"-"+str(row))
        res = map(int, "{:0128b}".format(int(v, 16)))
        row_sums.append(sum(res))
        for column, data in enumerate(res):
            node = Node(row, column, data)
            nodes.append(node)
            grid[row][column] = node

    for node in nodes:
        node.find_neighbours(grid)

    regions = []
    num_of_regions = 0
    for node in nodes:
        if node not in regions:
            region = node.get_region()
            if region:
                regions.extend(region)
                num_of_regions += 1

    print('Part 1: ', sum(row_sums))
    print('Part 2: ', num_of_regions)


if __name__ == '__main__':

    run_it('vbqugkhl')  # 8148, 1180
