import re


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):

    pattern = r'((\d)\2*)'
    number_seq = seq
    after_40 = 0
    for i in range(50):

        if i == 40:
            after_40 = len(number_seq)

        new_seq = ''
        for occ, value in re.findall(pattern, number_seq):
            new_seq += str(len(occ)) + value
        number_seq = new_seq

    print('Part 1: ', after_40)
    print('Part 2: ', len(number_seq))


if __name__ == '__main__':

    run_it("1113222113")  # 252594, 3579328
