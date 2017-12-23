

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


class Program(object):

    def __init__(self, pid):
        self.pid = pid
        self.neighbours = []

    def add_neighbour(self, program):
        self.neighbours.append(program)

    def get_group(self, group=None):
        if not group:
            group = []

        for neigh in self.neighbours:
            if neigh not in group:
                group.append(neigh)
                neigh.get_group(group)
        return group


def run_it(seq):
    rows = seq.split('\n')

    programs = []
    neighbours = {}
    for row in rows:
        program, neighs = row.split('<->')
        program = int(program.strip())
        programs.append(Program(program))
        neighbours[program] = neighs.strip()

    for prog, neighs in neighbours.items():
        neighs = [int(r.strip()) for r in neighs.split(',')]
        for program in programs:
            if program.pid == prog:
                for neighbour in neighs:
                    for n_program in programs:
                        if neighbour == n_program.pid:
                            program.add_neighbour(n_program)

    groups = []
    num_of_groups = 0
    for program in programs:
        if program not in groups:
            group = program.get_group()
            groups.extend(group)
            num_of_groups += 1

    print('Part 1: ', len(programs[0].get_group()))
    print('Part 2: ', num_of_groups)


if __name__ == '__main__':

    run_it(read_input())  # 130, 189
