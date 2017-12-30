

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):

    floor = 0
    position = 0
    entered = False
    for index, each in enumerate(seq):
        floor += 1 if each == '(' else -1
        if floor == -1 and not entered:
            position = index + 1
            entered = True

    print('Part 1: ', floor)
    print('Part 2: ', position)


if __name__ == '__main__':

    run_it(read_input())  # 232, 1783
