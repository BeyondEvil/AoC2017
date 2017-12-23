import numpy as np


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def parse(pattern):
    outer = []
    rows = pattern.split('/')
    for row in rows:
        inner = [i for i in row]
        outer.append(inner)
    return np.array(outer)


def find_match(master, rules):
    print "master in find:\n", master
    for each in rules:
        match = each[0]
        pattern = each[1]
        index = 0
        flipped = False
        while index < 4:
            if np.array_equal(master, match):
                return pattern
            match = np.rot90(match)
            index += 1
            if index == 3 and not flipped:
                match = np.fliplr(match)
                index = 0
                flipped = True


def run_it(seq):

    master_pattern = parse(".#./..#/###")

    print "pattern start:\n", master_pattern

    size2_rules = []
    size3_rules = []
    for rule in seq.split('\n'):
        match, transform = rule.split(' => ')
        m = parse(match)
        t = parse(transform)

        if m.size % 2 == 0:
            size2_rules.append((m, t))
        else:
            size3_rules.append((m, t))

    iterations = 1
    for i in range(iterations):
        if master_pattern.size % 2 == 0:
            match = find_match(master_pattern[0:2, 0:2], size2_rules)
            if match is not None:
                pass

        elif master_pattern.size % 3 == 0:
            match = find_match(master_pattern[0:3, 0:3], size3_rules)
            if match is not None:
                pass
        else:
            raise

    print "pattern finish:\n", master_pattern
    print "ons", np.count_nonzero(master_pattern == '#')

    print('Part 1: ', 0)
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it(read_input())  # ,
