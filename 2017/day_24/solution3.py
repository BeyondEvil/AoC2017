

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


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


def find_root(nodes):
    for node in nodes:
        if node.port_a == 0:
            return node


def get_sums(root, sums, sum, visited):
    if root not in visited:
        visited.add(root)
        sum += root.strength
        for neigh in root.neighbors:
            sums = get_sums(neigh, sums, sum, visited)
        sums.append(sum)
    return sums


def run_it(seq):

    nodes = list()
    for each in seq.split('\n'):
        p_a, p_b = each.split('/')
        p_a = int(p_a)
        p_b = int(p_b)
        nodes.append(Node(p_a, p_b))

    for node in nodes:
        node.find_neighbors(nodes)

    root = find_root(nodes)
    sums = get_sums(root, [], 0, set())
    print len(nodes)
    print len(sums)
    print max(sums)

    print('Part 1: ', 0)
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it(read_input())  # ,
