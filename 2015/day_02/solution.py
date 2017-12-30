

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    """l,w,h 2*l*w + 2*w*h + 2*h*l"""

    measurements = []
    for index, measurement in enumerate(seq.splitlines()):
        measurements.append(sorted(map(int, measurement.split('x'))))

    paper = 0
    ribbon = 0
    for each in measurements:
        l = each[0] * each[1]
        w = each[1] * each[2]
        h = each[2] * each[0]
        bow = each[0] * each[1] * each[2]
        ribbon += 2 * (each[0] + each[1]) + bow
        extra = min([l, w, h])
        total = 2 * (l + w + h) + extra
        paper += total

    print('Part 1: ', paper)
    print('Part 2: ', ribbon)


if __name__ == '__main__':

    run_it(read_input())  # 1598415, 3812909
