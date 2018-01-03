import re
from collections import defaultdict


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []

    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def run_it(seq):

    pattern = r'(?P<start>\w+)\s*to\s*(?P<dest>\w+)\s*=\s*(?P<weight>\d+)'
    components = defaultdict(set)
    weights = {}
    for pair in seq.splitlines():
        n1, n2, weight = re.findall(pattern, pair)[0]
        weights[(n1, n2)] = int(weight)
        weights[(n2, n1)] = int(weight)
        components[n1].add(n2)
        components[n2].add(n1)

    all_paths = set()
    for n1 in components.keys():
        for n2 in components.keys():
            paths = find_all_paths(components, n1, n2)
            for path in paths:
                if len(path) == len(components):
                    all_paths.add(tuple(path))

    sums = []
    for path in all_paths:
        _sum = 0
        for index, node in enumerate(path[:-1]):
            _sum += weights[(node, path[index + 1])]
        sums.append(_sum)

    print('Part 1: ', min(sums))
    print('Part 2: ', max(sums))


if __name__ == '__main__':

    run_it(read_input())  # 207, 804
