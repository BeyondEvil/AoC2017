
from collections import deque
from itertools import islice, izip_longest
from copy import copy
from functools import reduce
from operator import xor


def rotate(list_to_rotate, steps):
    if steps < 0:
        for _ in range(abs(steps)):
            list_to_rotate.append(list_to_rotate[0])
            del list_to_rotate[0]

    for _ in range(steps):
        list_to_rotate.insert(0, list_to_rotate.pop())


def reverse_sublist(lst, start, end):
    sublist = lst[start:end]
    sublist.reverse()
    lst[start:end] = sublist


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def run_it_a(_input):
    input_lengths = [int(i) for i in _input.split(',')]
    circular_list = range(256)
    print "start: ", circular_list

    rotation = 0
    for skip, length in enumerate(input_lengths):
        rotate(circular_list, rotation * -1)
        reverse_sublist(circular_list, 0, length)
        rotate(circular_list, rotation)
        rotation += length + skip

    print "finish: ", circular_list
    print "result: ", circular_list[0] * circular_list[1]


def run_it_a_deque(_input):
    input_lengths = [int(i) for i in _input.split(',')]
    circular_list = deque(range(256))
    print "start: ", circular_list

    rotation = 0
    for skip, length in enumerate(input_lengths):
        circular_list.rotate(rotation * -1)
        tmp_list = list(circular_list)
        reverse_sublist(tmp_list, 0, length)
        circular_list = deque(tmp_list)
        circular_list.rotate(rotation)
        rotation += length + skip

    print "finish: ", circular_list
    print "result: ", circular_list[0] * circular_list[1]


def run_it_b(_input):
    input_lengths = [ord(i) for i in _input]
    input_lengths.extend([17, 31, 73, 47, 23])
    circular_list = range(256)

    rounds = 64
    rotation = 0
    skip = 0
    print "Starting..."
    for index in range(rounds):
        for length in input_lengths:
            rotate(circular_list, rotation * -1)
            reverse_sublist(circular_list, 0, length)
            rotate(circular_list, rotation)
            rotation += length + skip
            skip += 1
        print "Round {} done!".format(index + 1)

    print "Sparse hash finished, starting dense hash..."
    block_size = 16
    dense_hash = []
    for chunk in grouper(circular_list, block_size):
        dense_hash.append(reduce(xor, chunk))

    print "Dense hash done!"

    return ''.join(map('{:02x}'.format, dense_hash))


def run_it_b_deque(_input):
    input_lengths = [ord(i) for i in _input]
    input_lengths.extend([17, 31, 73, 47, 23])
    circular_list = deque(range(256))

    rounds = 64
    rotation = 0
    skip = 0
    print "Starting..."
    for index in range(rounds):
        print "Round {} starting...".format(index + 1)
        for length in input_lengths:
            circular_list.rotate(rotation * -1)
            tmp_list = list(circular_list)
            reverse_sublist(tmp_list, 0, length)
            circular_list = deque(tmp_list)
            circular_list.rotate(rotation)
            rotation += length + skip
            skip += 1
        print "Round {} done!".format(index + 1)

    print "Sparse hash finished, starting dense hash..."
    block_size = 16
    dense_hash = []
    for chunk in grouper(circular_list, block_size):
        dense_hash.append(reduce(xor, chunk))

    print "Dense hash done!"

    return ''.join(map('{:02x}'.format, dense_hash))


if __name__ == '__main__':
    #puzzle_input = "3,4,1,5"
    puzzle_input = "197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63"

    #run_it_a(puzzle_input)
    #print run_it_b(puzzle_input)

    #assert run_it_b_deque("") == "a2582a3a0e66e6e86e3812dcb672a272"
    #assert run_it_b_deque("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    #assert run_it_b_deque("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    #assert run_it_b_deque("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

    #run_it_a(puzzle_input)
    print run_it_b_deque(puzzle_input)
