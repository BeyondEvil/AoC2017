with open("input.txt") as f:
    c = [list(map(int, line.split("/"))) for line in f]


def proper_name(components, start):
    highscore = 0
    high = []
    for comp in components:
        if comp[0] == start or comp[1] == start:
            cp_comp = components[:]
            cp_comp.remove(comp)
            x = comp + proper_name(cp_comp, comp[1] if comp[0] == start else comp[0])
            if sum(x) > highscore:
                highscore = sum(x)
                high = x

    return high


x = proper_name(c, 0)
print(sum(x))
