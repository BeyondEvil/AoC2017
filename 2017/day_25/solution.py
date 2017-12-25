
states = {('A', 0): {'value': 1, 'move': 'right', 'next': 'B'},
          ('A', 1): {'value': 0, 'move': 'right', 'next': 'C'},
          ('B', 0): {'value': 0, 'move': 'left', 'next': 'A'},
          ('B', 1): {'value': 0, 'move': 'right', 'next': 'D'},
          ('C', 0): {'value': 1, 'move': 'right', 'next': 'D'},
          ('C', 1): {'value': 1, 'move': 'right', 'next': 'A'},
          ('D', 0): {'value': 1, 'move': 'left', 'next': 'E'},
          ('D', 1): {'value': 0, 'move': 'left', 'next': 'D'},
          ('E', 0): {'value': 1, 'move': 'right', 'next': 'F'},
          ('E', 1): {'value': 1, 'move': 'left', 'next': 'B'},
          ('F', 0): {'value': 1, 'move': 'right', 'next': 'A'},
          ('F', 1): {'value': 1, 'move': 'right', 'next': 'E'}}


test_states = {('A', 0): {'value': 1, 'move': 'right', 'next': 'B'},
               ('A', 1): {'value': 0, 'move': 'left', 'next': 'B'},
               ('B', 0): {'value': 1, 'move': 'left', 'next': 'A'},
               ('B', 1): {'value': 1, 'move': 'right', 'next': 'A'}}


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):

    print('Part 1: ', 0)
    print('Part 2: ', 0)


if __name__ == '__main__':

    run_it(read_input())  # ,
