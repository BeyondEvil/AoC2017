

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def find_roots(components):
    roots = []
    for c in components:
        if 0 in c:
            roots.append(c)
    return roots


def get_compatible_components(match, comps):
    for c in comps:
        if match in c:
            yield c


def astar(components, start, end, visited, path):
    if start == end:
        path.append(start)
        return path

    visited.add(start)
    path.append(start)
    for c in get_compatible_components(start, components):
        components.remove(c)
        if c not in visited:
            path = astar(components, c, end, visited, path)
    return path


def astar2(components, start, end, visited, path):
    if end[0] == start or end[1] == start:
        path.append(end)
        cp_comp = components[:]
        cp_comp.remove(end)
        visited.add(end)
        for c in get_compatible_components(end[1] if end[0] == start else end[0], cp_comp):
            if c not in visited:
                path = astar2(cp_comp, end[1] if end[0] == start else end[0], c, visited, path)
    return path


def run_it(seq):

    components = []
    for component in seq.split('\n'):
        pa, pb = component.split('/')
        components.append((int(pa), int(pb)))

    bridges = []
    for comp in components:
        bridge = astar2(components[:], 0, comp, set(), [])
        if bridge:
            bridges.append(bridge)

    for bridge in bridges:
        print bridge
    print max([sum(map(sum, bridge)) for bridge in bridges])

 #   print('Part 1: ', 0)
  #  print('Part 2: ', 0)


if __name__ == '__main__':
    _seq = """0/1
10/1"""
    #run_it(_seq)

    _seq = """0/1
10/1
9/10"""
    #run_it(_seq)

    _seq = """0/2
0/1"""
    #run_it(_seq)

    _seq = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""
    run_it(_seq)

    run_it(read_input())  # ,
















