import hashlib


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):

    decimal = 0
    five = six = False
    while True:
        md5_hash = '{}{}'.format(seq, decimal)
        if hashlib.md5(md5_hash).hexdigest()[0:5].count('0') == 5 and not five:
            five = decimal
        if hashlib.md5(md5_hash).hexdigest()[0:6].count('0') == 6 and not six:
            six = decimal
        if five and six:
            break
        decimal += 1

    print('Part 1: ', five)
    print('Part 2: ', six)


if __name__ == '__main__':

    run_it("bgvyzdsv")  # 254575, 1038736
