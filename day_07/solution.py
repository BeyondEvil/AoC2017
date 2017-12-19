import re


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def find_root(nodes):
    for node in nodes:
        if node.is_root():
            return node


class Node(object):

    def __init__(self, name, weight=0, is_parent=False):
        self.name = name
        self.weight = weight
        self.total_weight = weight
        self.children_weights = []
        self.is_parent = is_parent
        self.parent = None
        self.children = []

    def is_root(self):
        return self.is_parent and not self.parent

    def is_leaf(self):
        return self.parent and not self.children

    def get_total_weight(self):
        if self.is_leaf():
            return self.weight
        total_weight = self.weight
        for child in self.children:
            total_weight += child.get_total_weight()
        return total_weight

    def get_heaviest_child(self):
        child_weights = {}
        for child in self.children:
            child_weights[child] = child.get_total_weight()
        weights = set(child_weights.values())
        if len(weights) == 1:
            return None
        value = max(child_weights.values())
        for child, weight in child_weights.items():
            if weight == value:
                return child


def run_it(seq):

    match = "\(|\)"
    nodes = set()
    parents = {}
    rows = seq.split('\n')

    # Add all nodes
    for row in rows:
        if '->' in row:  # root-node with n children:
            parent, children = row.split('->')
            parent_name, weight, _ = parent.split(' ')
            parent_weight = re.split(match, weight.strip())[1]
            node = Node(parent_name.strip(), int(parent_weight), is_parent=True)
            nodes.add(node)
            children = children.split(',')
            parents[parent_name] = [child.strip() for child in children]
        else:  # leaf w/o children:
            # leaf has a "weight", remove it for now
            child, weight = row.split(' ')
            weight = re.split(match, weight.strip())[1]
            node = Node(child.strip(), int(weight))
            nodes.add(node)

    # Map children and parents
    for parent, children in parents.items():
        # Find the parent Node
        for parent_node in nodes:
            if parent_node.name == parent:
                # find and add the children
                for child in children:
                    for child_node in nodes:
                        if child_node.name == child:
                            child_node.parent = parent_node
                            parent_node.children.append(child_node)

    root = find_root(nodes)
    print('Part 1: ', root.name)

    while True:
        new_root = root.get_heaviest_child()
        if new_root:
            root = new_root
        else:
            break

    weights = [c.get_total_weight() for c in root.parent.children]
    print('Part 2: ', root.weight - (max(weights) - min(weights)))


if __name__ == '__main__':

    run_it(read_input())  # vmpywg, 1674
