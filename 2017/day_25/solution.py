from collections import defaultdict

real_states = {('A', 0): (1, 1, 'B'),
               ('A', 1): (0, 1, 'C'),
               ('B', 0): (0, -1, 'A'),
               ('B', 1): (0, 1, 'D'),
               ('C', 0): (1, 1, 'D'),
               ('C', 1): (1, 1, 'A'),
               ('D', 0): (1, -1, 'E'),
               ('D', 1): (0, -1, 'D'),
               ('E', 0): (1, 1, 'F'),
               ('E', 1): (1, -1, 'B'),
               ('F', 0): (1, 1, 'A'),
               ('F', 1): (1, 1, 'E')}


def run_it(steps, states):
    tape = defaultdict(int)
    next_state = 'A'
    index = 0
    for step in range(steps):
        value, direction, next_state = states.get((next_state, tape.get(index, 0)))
        tape[index] = value
        index += direction

    print('Part 1: ', sum(tape.values()))


if __name__ == '__main__':

    run_it(12399302, real_states)  # 2794,
