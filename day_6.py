def run_it_a(sequence):

    sequence = [int(num) for num in sequence.split('\t')]
    seen = [hash(','.join(str(sequence)))]
    sequence_length = len(sequence)

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
        redistributions += 1
        current_hash = hash(','.join(str(sequence)))
        if current_hash in seen:
            break
        seen.append(current_hash)

    return redistributions


def run_it_b(sequence):

    sequence = [int(num) for num in sequence.split('\t')]
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
        redistributions += 1
        current_hash = hash(','.join(str(sequence)))
        if current_hash in seen:
            if seen_once:
                break
            seen_once = True
            seen = []
            redistributions = 0
        seen.append(current_hash)

    return redistributions


if __name__ == '__main__':
    _sequence2 = """0\t2\t7\t0"""
    _sequence = """0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"""

    #print run_it_a(_sequence)

    print run_it_b(_sequence)
