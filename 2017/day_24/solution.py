
def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


class Component(object):

    class Port(object):
        def __init__(self, strength):
            self.strength = strength
            self.free = True

    def __init__(self, port_a, port_b):
        self.port_a = self.Port(port_a)
        self.port_b = self.Port(port_b)
        self.used = False
        self.total_strength = self.total_strength()

    def __repr__(self):
        return "port a: {0.port_a.strength}\nport b: {0.port_b.strength}\n".format(self)

    def total_strength(self):
        return self.port_a.strength + self.port_b.strength

    def has_free_ports(self):
        return self.port_a.free or self.port_b.free

    def get_free_port(self, strength):
        if self.port_a.strength == strength and self.port_a.free:
            return self.port_a
        if self.port_b.strength == strength and self.port_b.free:
            return self.port_b
        return None


def run_it(seq):

    components = list()
    for each in seq.split('\n'):
        p_a, p_b = each.split('/')
        components.append(Component(int(p_a), int(p_b)))

    match = 0
    used = []
    components.sort(key=lambda x: x.total_strength, reverse=True)
    index = 0
    while index < 300:
        for component in components:
            if component not in used:
                port = component.get_free_port(match)
                if port:
                    port.free = False
                    if component.port_a.strength != match:
                        match = component.port_a.strength
                    elif component.port_b.strength != match:
                        match = component.port_b.strength
                    else:
                        assert False
                    component.used = True
                    used.append(component)
        index += 1

    sum = 0
    for each in used:
        sum += each.total_strength

    print sum


    print('Part 1: ', 0)
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it(read_input())  # ,
