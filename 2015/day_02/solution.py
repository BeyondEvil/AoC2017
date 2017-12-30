

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    """l,w,h 2*l*w + 2*w*h + 2*h*l"""

    measurements = []
    for measurement in seq.splitlines():
        measurements.append(sorted(map(int, measurement.split('x'))))

    paper = 0
    ribbon = 0
    for l, w, h in measurements:
        area = [l * w, w * h, h * l]
        paper += 2 * sum(area) + min(area)
        ribbon += 2 * (l + w) + (l * w * h)

    print('Part 1: ', paper)
    print('Part 2: ', ribbon)


if __name__ == '__main__':

    run_it(read_input())  # 1598415, 3812909
