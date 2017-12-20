

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    garbage_mode = False
    ignore_mode = False
    canceled_chars = 0
    garbage_chars = 0
    score = []
    char_stack = []
    for char in seq:
        if not ignore_mode:
            if garbage_mode:
                garbage_chars += 1
            if not garbage_mode:
                if char == '{':
                    char_stack.append(char)
                if char == '}':
                    score.append(len(char_stack))
                    char_stack.pop()
            if char == '<':
                garbage_mode = True
            if char == '>':
                garbage_chars -= 1
                garbage_mode = False
            if char == '!':
                ignore_mode = True
        else:
            canceled_chars += 1
            ignore_mode = False

    print('Part 1: ', sum(score))
    print('Part 2: ', garbage_chars - canceled_chars)


if __name__ == '__main__':

    run_it(read_input())  # 14212, 6569
