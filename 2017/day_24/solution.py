from collections import defaultdict


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def gen_bridges(components, bridge):
    cur_port = bridge[-1][1]
    for next_port in components[cur_port]:
        component = (cur_port, next_port)
        if not (component in bridge or component[::-1] in bridge):
            new = bridge + [component]
            yield new
            for each in gen_bridges(components, new):
                yield each


def run_it(seq):
    components = defaultdict(set)
    for comp in seq.strip().splitlines():
        p1, p2 = [int(p) for p in comp.split('/')]
        components[p1].add(p2)
        components[p2].add(p1)

    bridge_meta = []
    for bridge in gen_bridges(components, [(0, 0)]):
        bridge_meta.append((len(bridge), sum(a+b for a, b in bridge)))

    print('Part 1: ', sorted(bridge_meta, key=lambda x: x[1])[-1][1])
    print('Part 2: ', sorted(bridge_meta)[-1][1])


if __name__ == '__main__':

    run_it(read_input())  # 1695, 1673
