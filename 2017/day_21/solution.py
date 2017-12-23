import numpy as np
from math import sqrt


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def parse(pattern):
    pattern = pattern.replace('/', '')
    size = int(sqrt(len(pattern)))
    return np.array([1 if c == '#' else 0 for c in pattern], dtype=int).reshape(size, size)


def build_list(rule, enhance, rules):
    seen = rules.keys()
    for i in range(8):
        hash_rule = tuple(rule.flatten())
        if hash_rule not in seen:
            rules[hash_rule] = enhance
        rule = np.rot90(rule)
        if i == 3:
            rule = np.fliplr(rule)


def find_match(pattern, rules):
    for hash_rule, enhance in rules.items():
        if tuple(pattern.flatten()) == hash_rule:
            return enhance.copy()


def transform(array, rules, sizer, stepper):
    steps = len(array) / sizer
    new_grid = np.zeros((stepper * steps, stepper * steps), dtype=int)
    for row in range(steps):
        for col in range(steps):
            rule = array[sizer * row:sizer * row + sizer, sizer * col:sizer * col + sizer].copy()
            enhance = find_match(rule, rules)
            if enhance is not None:
                new_grid[stepper * row:stepper * row + stepper, stepper * col:stepper * col + stepper] = enhance.copy()

    return new_grid


def run_it(seq, iterations):

    master_pattern = ".#./..#/###"
    art = parse(master_pattern)

    size2_rules = dict()
    size3_rules = dict()
    for pair in seq.split('\n'):
        rule, enhance = pair.split(' => ')
        a_rule = parse(rule)
        a_enhance = parse(enhance)
        if a_rule.size % 2 == 0:
            build_list(a_rule, a_enhance, size2_rules)
        elif a_rule.size % 3 == 0:
            build_list(a_rule, a_enhance, size3_rules)
        else:
            raise

    part_1 = 0
    for i in range(iterations):
        print "Iteration: ", i + 1

        if i == 5:
            part_1 = art.sum()

        size = len(art)
        if size % 2 == 0:
            art = transform(art, size2_rules, 2, 3)
        elif size % 3 == 0:
            art = transform(art, size3_rules, 3, 4)
        else:
            raise

    print('Part 1: ', int(part_1))
    print('Part 2: ', int(art.sum()))


if __name__ == '__main__':

    run_it(read_input(), 18)  # 205, 3389823
