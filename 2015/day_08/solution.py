import re


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):

    ascii_pattern = r'\\x\w{2}'
    total = 0
    for literal in seq.splitlines():
        code_size = len(literal)
        literal = literal.replace('\\\\', 'A')\
            .replace('\\"', 'A')\
            .replace('"', '')
        literal = re.sub(ascii_pattern, 'A', literal)
        string_size = len(literal)
        total += code_size - string_size

    print('Part 1: ', total)
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it(read_input())  # 1333,
