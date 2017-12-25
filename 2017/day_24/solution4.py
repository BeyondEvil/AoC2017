import networkx as nx


class Node(object):

    def __init__(self, port_a, port_b):
        self.port_a = port_a
        self.port_b = port_b
        self.strength = port_a + port_b
        self.neighbors = []

    def __repr__(self):
        return "{0.port_a}/{0.port_b}".format(self)

    def find_neighbors(self, nodes):
        for node in nodes:
            if node != self:
                if node.port_a in [self.port_a, self.port_b] or \
                                node.port_b in [self.port_a, self.port_b]:
                    self.neighbors.append(node)


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def get_strength(graph, path):
    return graph.subgraph(path).size('weight')


def run_it(seq):

    nodes = list()
    for each in seq.split('\n'):
        p_a, p_b = each.split('/')
        p_a = int(p_a)
        p_b = int(p_b)
        nodes.append(Node(p_a, p_b))

    for node in nodes:
        node.find_neighbors(nodes)

    graph = nx.Graph()

    for node in nodes:
        graph.add_node(node.strength)
        for neigh in node.neighbors:
            graph.add_edge(node.strength, neigh.strength)

    strengths = []
    for path in nx.all_simple_paths(graph, min(graph.nodes()), max(graph.nodes())):
        strengths.append(get_strength(graph, path))
        print strengths
    print max(strengths)

    print('Part 1: ', 0)
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it(read_input())  # ,
