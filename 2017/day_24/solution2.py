import networkx as nx


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def get_strength(graph, path):
    return graph.subgraph(path).size('weight')


def run_it(seq):

    graph = nx.Graph()
    start = 0
    end = 0
    nodes = set()
    for each in seq.split('\n'):
        p_a, p_b = each.split('/')
        p_a = int(p_a)
        p_b = int(p_b)
        nodes.add(p_a)
        nodes.add(p_b)
        if p_a >= end:
            end = p_a
        if p_b >= end:
            end = p_b
        graph.add_edge(p_a, p_b, weight=(p_a + p_b))

    print graph.subgraph([0, 30, 2, 13, 20, 36, 4, 16, 14, 42, 11, 5, 29, 41, 44, 6, 15, 23, 39, 35, 50, 24, 46, 31]).size('weight')

    strengths = []
    for node in nodes:
        for path in nx.all_simple_paths(graph, 0, node):
            strengths.append(get_strength(graph, path))
    print max(strengths)
    exit(0)
    strengths = []
    seen = set()
    for edge in graph.edges():
        for path in nx.all_simple_paths(graph, start, edge[0]):
            if tuple(path) not in seen:
                seen.add(tuple(path))
                strengths.append(get_strength(graph, path))
                if 1695 in strengths:
                    print "1695", edge, path
                if 2006 in strengths:
                    print "2006", edge, path
        for path in nx.all_simple_paths(graph, start, edge[1]):
            if tuple(path) not in seen:
                seen.add(tuple(path))
                strengths.append(get_strength(graph, path))
                if 1695 in strengths:
                    print "1695", edge, path
                if 2006 in strengths:
                    print "2006", edge, path


    if 1695 in strengths:
        print "YES"
    print max(strengths)
    print('Part 1: ', 0)
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it(read_input())  # ,
