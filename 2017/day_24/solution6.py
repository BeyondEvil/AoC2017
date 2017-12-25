

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def get_compatible_components(match, comps):
    for c in comps:
        if match in c:
            yield c
    return


def run_it(seq):

    components = []
    for component in seq.split('\n'):
        pa, pb = component.split('/')
        components.append((int(pa), int(pb)))

    start = None
    for comp in components:
        if comp[0] == 0:
            start = comp

    closed_set = set()
    open_set = set()
    current = start
    port = 1
    open_set.add(current)
    total_sum = sum(current)
    iterations = 0
    while open_set:
        if iterations > 10000:
            break
        current = max(open_set, key=lambda x: sum(x))
        open_set.remove(current)
        closed_set.add(current)
        connected_sum = 0
        last = current
        for c in get_compatible_components(current[port], components):

            if c in closed_set:
                continue

            if c not in open_set:
                open_set.add(c)

            if sum(c) > connected_sum:
                connected_sum = sum(c)
                last = c

        if current[port] == last[0]:
            port = 1
        elif current[port] == last[1]:
            port = 0
        else:
            assert False
        total_sum += connected_sum
        iterations += 1

    print total_sum
    print closed_set
    print('Part 1: ', 0)
    print('Part 2: ', 0)


if __name__ == '__main__':
    _seq = """0/1
10/1
9/10"""
    run_it(_seq)

    _seq = """0/3
3/7
7/4"""
    run_it(_seq)
    run_it(read_input())  # ,
