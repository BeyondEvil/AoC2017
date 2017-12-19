def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    sequence = [int(index) for index in seq.split('\n')]
    jump = sequence[0]
    jumps_made = 0
    while True:
        try:
            if jump == 0:  # Do nothing
                next_index = sequence[jump]
                sequence[jump] += 1
                jump = next_index

            elif jump > 0:  # Move forward
                next_index = sequence[jump]
                sequence[jump] += 1
                jump += next_index

            elif jump < 0:  # Move backwards
                next_index = sequence[jump]
                sequence[jump] += 1
                jump -= next_index
            if jump:
                jumps_made += 1

        except IndexError:
            jumps_made += 1
            break

    print('Part 1: ', jumps_made)

    sequence = [int(index) for index in seq.split('\n')]
    jump = sequence[0]
    jumps_made = 0
    while True:
        try:

            if jump == 0:  # Do nothing
                next_index = sequence[jump]
                sequence[jump] += 1
                jump = next_index

            elif jump > 0:  # Move forward
                next_index = sequence[jump]
                if next_index >= 3:
                    sequence[jump] -= 1
                else:
                    sequence[jump] += 1
                jump += next_index

            elif jump < 0:  # Move backwards
                next_index = sequence[jump]
                sequence[jump] += 1
                jump -= next_index
            if jump:
                jumps_made += 1

        except IndexError:
            jumps_made += 1
            break

    print('Part 2: ', jumps_made)


if __name__ == '__main__':

    run_it(read_input())  # 378980, 26889114
