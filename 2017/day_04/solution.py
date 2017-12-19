def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    valid_phrases = []
    for row in seq.split('\n'):
        words = row.split(' ')
        num_words = len(words)
        words_set = set(words)
        num_unique = len(words_set)
        if num_words == num_unique:
            valid_phrases.append(row)

    sorted_valid_phrases = []
    for phrase in valid_phrases:
        words = phrase.split(' ')
        len_before = len(words)
        sorted_words = set()
        for word in words:
            sorted_words.add(''.join(sorted(word)))
        len_after = len(sorted_words)
        if len_after == len_before:
            sorted_valid_phrases.append(phrase)

    print('Part 1: ', len(valid_phrases))
    print('Part 2: ', len(sorted_valid_phrases))


if __name__ == '__main__':

    run_it(read_input())  # 325, 119
