from collections import deque
from itertools import izip_longest
from functools import reduce
from operator import xor


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def reverse_sublist(lst, start, end):
    sublist = lst[start:end]
    sublist.reverse()
    lst[start:end] = sublist


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def run_it(seq):
    input_lengths = [int(i) for i in seq.split(',')]
    circular_list = deque(range(256))

    rotation = 0
    for skip, length in enumerate(input_lengths):
        circular_list.rotate(rotation * -1)
        tmp_list = list(circular_list)
        reverse_sublist(tmp_list, 0, length)
        circular_list = deque(tmp_list)
        circular_list.rotate(rotation)
        rotation += length + skip

    print('Part 1: ', circular_list[0] * circular_list[1])


def run_it2(seq):
    input_lengths = [ord(i) for i in seq]
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

    print('Part 2: ', ''.join(map('{:02x}'.format, dense_hash)))


if __name__ == '__main__':

    run_it(read_input())  # 40132
    run_it2(read_input())  # 35b028fe2c958793f7d5a61d07a008c8
