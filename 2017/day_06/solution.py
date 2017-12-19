def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    sequence = [int(num) for num in seq.split('\t')]
    seen = [hash(','.join(str(sequence)))]
    sequence_length = len(sequence)

    seen_once = False
    redistributions = 0
    while True:
        max_value = max(sequence)
        index_of_max = sequence.index(max_value)
        sequence[index_of_max] = 0
        index_of_max = (index_of_max + 1) % sequence_length
        while max_value > 0:
            sequence[index_of_max] += 1
            max_value -= 1
            index_of_max = (index_of_max + 1) % sequence_length
        current_hash = hash(','.join(str(sequence)))
        if current_hash in seen:
            if seen_once:
                break
            seen_once = True
            redistributions = len(seen)
            seen = []
        seen.append(current_hash)

    print('Part 1: ', redistributions)
    print('Part 2: ', len(seen))


if __name__ == '__main__':

    run_it(read_input())  # 7864, 1695
