from collections import defaultdict


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):

    vowels = ['a', 'e', 'i', 'o', 'u']
    verboten = ['ab', 'cd', 'pq', 'xy']
    nice = 0
    for word in seq.splitlines():
        double = False
        vowel = 0
        try:
            for v in verboten:
                if v in word:
                    raise SyntaxError
        except SyntaxError:
            continue
        for index, char in enumerate(word[:-1]):
            if char == word[index + 1]:
                double = True
        for char in word:
            if char in vowels:
                vowel += 1
        if double and vowel >= 3:
            nice += 1

    print('Part 1: ', nice)

    nice = 0
    for word in seq.splitlines():
        sequences = defaultdict(int)
        triple = []
        overlap = ''
        repeat = False
        sequence = False

        for char in word:
            if not triple:
                triple.append(char)
            elif char in triple:
                triple.append(char)
                if len(triple) == 3:
                    overlap = 3*char
                if len(triple) > 3:
                    overlap = ''
            else:
                triple = list()
                triple.append(char)

        for index, char in enumerate(word[:-2]):
            if char == word[index + 2]:
                repeat = True

        if repeat:
            for index, char in enumerate(word[:-1]):
                pair = char + word[index + 1]
                if pair not in overlap:
                    sequences[pair] += 1
            for occ in sequences.values():
                if occ >= 2:
                    sequence = True

        if repeat and sequence:
            nice += 1

    print('Part 2: ', nice)


if __name__ == '__main__':

    run_it(read_input())  # 238, 69
