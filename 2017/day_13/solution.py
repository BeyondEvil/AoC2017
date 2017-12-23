from copy import copy


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
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

    orig_fw = copy(firewall)

    severities = []
    for index, layer in enumerate(firewall):
        if layer == 0:
            severities.append(index * ((depths[index] / 2) + 1))
        for f_index, _ in enumerate(firewall):
            if firewall[f_index] != -1:
                firewall[f_index] = (firewall[f_index] + 1) % depths[f_index]

    def forward(fw, steps):
        for i, _ in enumerate(fw):
            if firewall[i] != -1:
                firewall[i] = (firewall[i] + steps) % depths[i]

    fresh_state = copy(orig_fw)
    moves = 0
    while True:
        success = True
        firewall = copy(fresh_state)
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

    print('Part 1: ', sum(severities))
    print('Part 2: ', moves)


if __name__ == '__main__':

    run_it(read_input())  # 1728, 3946838
