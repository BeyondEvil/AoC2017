
class Sentinel(object):

    def __init__(self, layer, depth):
        self.layer = layer
        self.depth = depth
        self.current_pos = 0
        self.direction = 1

    def __repr__(self):
        return "\nCurrent pos: " + str(self.current_pos) + "\tDepth: " + str(self.depth)
        #return "\nLayer: " + str(self.layer) + "\nDepth: " + str(self.depth) + "\nCurrent pos: " + str(self.current_pos)

    def move(self):
        if self.direction == 1:
            self.current_pos += 1
            if self.current_pos == self.depth - 1:
                self.direction = 0

        elif self.direction == 0:
            self.current_pos -= 1
            if self.current_pos == 0:
                self.direction = 1


def do_it(_firewall, _sentinels):
    for index, layer in enumerate(_firewall):
        for sentinel in _sentinels:
            if sentinel.current_pos == 0 and sentinel.layer == index:
                return False
            sentinel.move()
    return True


def reset(_sentinels):
    for sentinel in _sentinels:
        sentinel.current_pos = 0
        sentinel.direction = 1


def step(_steps, _sentinels):
    for _ in range(_steps):
        for sentinel in _sentinels:
            sentinel.move()


def run_it_a(seq):

    data = {}
    sentinels = []
    for row in seq.split('\n'):
        layer, depth = row.split(':')
        layer = int(layer.strip())
        depth = int(depth.strip())
        data[layer] = depth
        sentinels.append(Sentinel(layer, depth))

    length = max(data.keys())

    firewall = []
    for layer in range(length + 1):
        firewall.append([i for i in range(data.get(layer, 0))])

    severities = []
    for index, layer in enumerate(firewall):
        for sentinel in sentinels:
            if sentinel.current_pos == 0 and sentinel.layer == index:
                severities.append(index * len(layer))
            sentinel.move()

    print sum(severities)


def run_it_a_alternative(seq):
    index = 0
    firewall = []
    depths = []
    for row in seq.split('\n'):
        layer, depth = row.split(':')
        layer = int(layer.strip())
        depth = int(depth.strip())
        depth = (depth - 1) * 2
        while index < layer:
            firewall.append(-1)
            depths.append(-1)
            index += 1
        index += 1
        firewall.append(0)
        depths.append(depth)

    severities = []
    for index, layer in enumerate(firewall):
        if layer == 0:
            severities.append(index * ((depths[index] / 2) + 1))
        for f_index, _ in enumerate(firewall):
            if firewall[f_index] != -1:
                firewall[f_index] = (firewall[f_index] + 1) % depths[f_index]

    print(sum(severities))


def run_it_b(seq):
    import copy

    index = 0
    firewall = []
    depths = []
    for row in seq.split('\n'):
        layer, depth = row.split(':')
        layer = int(layer.strip())
        depth = int(depth.strip())
        depth = (depth - 1) * 2
        while index < layer:
            firewall.append(-1)
            depths.append(-1)
            index += 1
        index += 1
        firewall.append(0)
        depths.append(depth)

    def forward(list, steps):
        for index, _ in enumerate(list):
            if firewall[index] != -1:
                firewall[index] = (firewall[index] + steps) % depths[index]

    fresh_state = copy.copy(firewall)
    moves = 0
    while True:
        success = True
        firewall = copy.copy(fresh_state)
        forward(firewall, moves)
        for index, layer in enumerate(firewall):
            if layer == 0:
                success = False
                break
            for f_index, _ in enumerate(firewall):
                if firewall[f_index] != -1:
                    firewall[f_index] = (firewall[f_index] + 1) % depths[f_index]
        if success:
            break
        moves += 1

    print(moves)


if __name__ == '__main__':

    _seq = """0: 3
1: 2
4: 4
6: 4"""

    _seq = """0: 3
1: 2
2: 4
4: 8
6: 5
8: 6
10: 6
12: 4
14: 6
16: 6
18: 9
20: 8
22: 8
24: 8
26: 8
28: 10
30: 8
32: 12
34: 10
36: 14
38: 12
40: 12
42: 12
44: 12
46: 12
48: 12
50: 14
52: 12
54: 14
56: 12
58: 12
60: 14
62: 18
64: 14
68: 14
70: 14
72: 14
74: 14
78: 14
80: 20
82: 14
84: 14
90: 17"""

    #run_it_a(_seq)
    run_it_b(_seq)
