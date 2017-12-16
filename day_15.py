import binascii


def run_it_a(start_a, start_b):
    iterations = int(40e6)
    factor_a = 16807
    factor_b = 48271
    product = 2147483647
    matches = 0
    for iteration in range(iterations):
        _, start_a = divmod(start_a * factor_a, product)
        _, start_b = divmod(start_b * factor_b, product)
        mask = (1 << 16) - 1
        res_a = '{:08b}'.format(start_a & mask)
        res_b = '{:08b}'.format(start_b & mask)
        if res_a == res_b:
            matches += 1

    print matches


def get_value(start, factor, product, condition):
    while True:
        _, start = divmod(start * factor, product)
        if start % condition == 0:
            yield start


def run_it_b(start_a, start_b):
    iterations= int(5e6)
    factor_a = 16807
    factor_b = 48271
    product = 2147483647
    mask = (1 << 16) - 1
    matches = 0

    for _ in range(iterations):
        start_a = next(get_value(start_a, factor_a, product, 4))
        start_b = next(get_value(start_b, factor_b, product, 8))
        res_a = '{:08b}'.format(start_a & mask)
        res_b = '{:08b}'.format(start_b & mask)
        if res_a == res_b:
            matches += 1

    print matches


if __name__ == '__main__':

    #run_it_a(618, 814)
    run_it_b(618, 814)
