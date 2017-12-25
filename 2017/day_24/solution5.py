

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def build(components, component, strength, visited, bridges):
    if component not in visited:
        visited.add(component)
        strength += sum(component)
        bridges.append(strength)
        for c in components:
            if component[0] in c or component[1] in c:
                bridges = build(components, c, strength, visited, bridges)
    return bridges


def run_it(seq):

    components = []
    for component in seq.split('\n'):
        pa, pb = component.split('/')
        components.append((int(pa), int(pb)))

    start = None
    for comp in components:
        if comp[0] == 0:
            start = comp

    bridges = build(components, start, 0, set(), [])
    print max(bridges)

    print('Part 1: ', 0)
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it(read_input())  # ,
