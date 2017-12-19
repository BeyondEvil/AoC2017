def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    size = len(seq)

    next_all = 1
    keep_all = []

    skip = int(size / 2)
    next_skip = skip
    keep_skip = []

    for index, each in enumerate(seq):
        if next_all == size:
            next_all = 0
        if each == seq[next_all]:
            keep_all.append(each)
        if each == seq[next_skip]:
            keep_skip.append(each)
        next_all += 1
        next_skip = ((index + 1) + skip) % size

    print('Part 1: ', sum(map(int, keep_all)))
    print('Part 2: ', sum(map(int, keep_skip)))


if __name__ == '__main__':

    run_it(read_input())  # 1141, 950
