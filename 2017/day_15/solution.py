

def get_value(start, factor, product, condition):
    while True:
        start = (start * factor) % product
        if start % condition == 0:
            yield start


def run_it(start_a, start_b):
    iterations = int(40e6)
    factor_a = 16807
    factor_b = 48271
    product = 2147483647
    matches_a = 0
    mask = (1 << 16) - 1  # 65535
    a = start_a
    b = start_b
    for iteration in range(iterations):
        a = (a * factor_a) % product
        b = (b * factor_b) % product
        if a & mask == b & mask:
            matches_a += 1

    iterations = int(5e6)
    matches_b = 0
    a = start_a
    b = start_b
    for _ in range(iterations):
        a = next(get_value(a, factor_a, product, 4))
        b = next(get_value(b, factor_b, product, 8))
        if a & mask == b & mask:
            matches_b += 1

    print('Part 1: ', matches_a)
    print('Part 2: ', matches_b)


if __name__ == '__main__':

    run_it(618, 814)  # 577, 316
