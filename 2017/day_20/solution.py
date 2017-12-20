import re
import operator
from functools import reduce


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    particles = dict()
    for index, particle in enumerate(seq.split('\n')):
        values = particle.split(', ')
        metrics = [reduce(operator.add, map(abs, map(int, re.findall('[-]?\d+', v, re.M)))) for v in values]
        particles[index] = metrics

    sorted_list = sorted(particles.values(), key=operator.itemgetter(2, 1, 0))
    slowest = None
    for particle, data in particles.items():
        if data == sorted_list[0]:
            slowest = particle
            break

    print('Part 1: ', slowest)


class Particle(object):

    def __init__(self, name, p, v, a):
        self.name = name
        self.p = p
        self.v = v
        self.a = a
        self.collided = False

    def move(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]


def run_it2(seq):
    particles = list()
    for index, particle in enumerate(seq.split('\n')):
        values = particle.split(', ')
        metrics = [list(map(int, re.findall('[-]?\d+', v, re.M))) for v in values]
        particles.append(Particle(index, *metrics))

    collisions = set()
    for tick in range(100):
        for index, p_one in enumerate(particles[:-1]):
            for p_two in particles[index + 1:]:
                if p_one.p == p_two.p:
                    p_one.collided = True
                    p_two.collided = True

        for particle in particles:
            if particle.collided:
                collisions.add(particle)
            else:
                particle.move()

    print('Part 2: ', len(set(particles).difference(collisions)))


if __name__ == '__main__':
    run_it(read_input())  # 300,
    run_it2(read_input())  # 502
