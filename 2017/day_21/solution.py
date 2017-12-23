import numpy as np


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def parse(pattern):
    if len(pattern) == 5:
        r = c = 2
    elif len(pattern) == 11:
        r = c = 3
    elif len(pattern) == 19:
        r = c = 4
    else:
        raise

    array = np.zeros((r, c), dtype=int)
    r = c = 0
    for char in pattern:
        if char == '#':
            array[r, c] = 1
        elif char == '/':
            r += 1
            c = -1
        c += 1

    return array


def build_list(rule, enhance, rules):
    index = 0
    flipped = False
    seen = rules.keys()
    while index < 4:
        hash_rule = tuple(rule.flatten())
        if hash_rule not in seen:
            rules[hash_rule] = enhance
        rule = np.rot90(rule)
        index += 1
        if index == 4 and not flipped:
            rule = np.fliplr(rule)
            index = 0
            flipped = True


def find_match(pattern, rules):
    for hash_rule, enhance in rules.items():
        if tuple(pattern.flatten()) == hash_rule:
            return enhance.copy()


def transform(array, rules, sizer, stepper):
    size = len(array)
    steps = size / sizer
    new_grid = np.zeros((stepper * steps, stepper * steps))
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
