from collections import deque


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def swap(programs, ia, ib):
    programs[int(ia)], programs[int(ib)] = programs[int(ib)], programs[int(ia)]


def dance(programs, moves):

    programs = list(programs)
    for move in moves:
        if move.startswith('s'):
            d = deque(programs)
            d.rotate(int(move[1:]))
            programs = list(d)
        elif move.startswith('x'):
            move = move[1:]
            ia, ib = move.split('/')
            swap(programs, ia, ib)
        elif move.startswith('p'):
            move = move[1:]
            ia, ib = move.split('/')
            ia = programs.index(ia)
            ib = programs.index(ib)
            swap(programs, ia, ib)

    return programs


def run_it(seq):
    moves = seq.strip().split(',')
    programs = "abcdefghijklmnop"
    part_1 = ''.join(dance(programs, moves))

    reps = int(1e9)
    seen = []
    part_2 = None
    for i in range(reps):
        p = ''.join(programs)
        if p not in seen:
            programs = dance(programs, moves)
            seen.append(p)
        else:
            part_2 = seen[reps % i]
            break

    print('Part 1: ', part_1)
    print('Part 2: ', part_2)


if __name__ == '__main__':

    run_it(read_input())  # fgmobeaijhdpkcln, lgmkacfjbopednhi
