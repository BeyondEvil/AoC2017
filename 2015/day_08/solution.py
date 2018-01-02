import re


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def in_memory(text):
    ascii_pattern = r'\\x\w{2}'
    text = text.replace('\\\\', 'A') \
        .replace('\\"', 'A') \
        .replace('"', '')
    return re.sub(ascii_pattern, 'A', text)


def encoded(text):
    text = text.replace('\\', '\\\\') \
        .replace('"', '\\"')
    return '"' + text + '"'


def run_it(seq):
    memorized = 0
    encoderized = 0
    for literal in seq.splitlines():
        code_size = len(literal)

        in_mem = in_memory(literal)
        memorized += code_size - len(in_mem)

        enc = encoded(literal)
        encoderized += len(enc) - code_size

    print('Part 1: ', memorized)
    print('Part 2: ', encoderized)


if __name__ == '__main__':

    run_it(read_input())  # 1333, 2046
