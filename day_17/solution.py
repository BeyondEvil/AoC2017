def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    steps = int(seq)
    insertions = int(50e6)
    buffer_list = [0]
    current_pos = 0
    moment_a = 0
    moment_b = 0
    for value in range(insertions):
        next_pos = (current_pos + steps) % (value + 1)
        next_pos += 1
        if value < 2017:
            buffer_list.insert(next_pos, value + 1)
            moment_a = next_pos + 1
        if next_pos == 1:
            moment_b = value + 1
        current_pos = next_pos

    print('Part 1: ', buffer_list[moment_a])
    print('Part 2: ', moment_b)


if __name__ == '__main__':

    run_it(read_input())  # 1306, 20430489
