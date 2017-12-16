def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


def run_it(seq):
    result = seq.split('\n')
    outer = []
    for each in result:
        res = each.split('\t')
        inner = []
        for r in res:
            inner.append(int(r))
        outer.append(inner)

    result_list = []
    for each in outer:
        size = len(each)
        inner = []
        for index_a, value in enumerate(each):
            index_b = index_a + 1
            if size == index_b:
                break

            while index_b < size:
                if value % each[index_b] == 0 or each[index_b] % value == 0:
                    inner.append(value)
                    inner.append(each[index_b])
                    break
                index_b += 1
        result_list.append(max(inner) / min(inner))

    print('Part 1: ', sum(map(lambda a: (max(a) - min(a)) if a else 0, outer)))
    print('Part 2: ', sum(result_list))


if __name__ == '__main__':

    run_it(read_input())  # 34581, 214
