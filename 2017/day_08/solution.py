from collections import defaultdict
import operator as op


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    operators = {'>': op.gt,
                 '<': op.lt,
                 '>=': op.ge,
                 '<=': op.le,
                 '==': op.eq,
                 '!=': op.ne,
                 'inc': op.iadd,
                 'dec': op.isub}

    registry = defaultdict(int)
    largest = 0
    for row in seq.split('\n'):
        register_to_modify, operation, op_value, conditional, conditional_reg, operator, cond_value = row.split(' ')
        if operators[operator](registry[conditional_reg], int(cond_value)):
            registry[register_to_modify] = operators[operation](registry[register_to_modify], int(op_value))
        if registry[register_to_modify] >= largest:
            largest = registry[register_to_modify]

    print('Part 1: ', max(registry.values()))
    print('Part 2: ', largest)


if __name__ == '__main__':

    run_it(read_input())  # 2971, 4254
