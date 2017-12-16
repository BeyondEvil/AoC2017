def run_it_a(row):
    return max(row) - min(row)


def run_it_b(row):
    _sum = 0
    size = len(captcha)
    skip = size / 2
    _next = skip
    keep = []
    index = 0
    for each in captcha:
        if each == captcha[_next]:
            keep.append(each)
        index += 1
        _next = (index + skip) % size

    for each in keep:
        _sum += int(each)

    return _sum


def do_it_a(spreadsheet):
    result = spreadsheet.split('\n')
    outer = []
    for each in result:
        res = each.split('\t')
        inner = []
        for r in res:
            inner.append(int(r))
        outer.append(inner)

    _sum = sum([run_it_a(each) for each in outer if each])
    print("SUM: ", _sum)
    return _sum


def do_it_b(spreadsheet):
    result = spreadsheet.split('\n')
    outer = []
    for each in result:
        res = each.split('\t')
        inner = []
        for r in res:
            inner.append(int(r))
        outer.append(inner)

    print outer
    result_list = []
    for each in outer:
        size = len(each)
        inner = []
        for index_a, value in enumerate(each):
            index_b = index_a + 1
            if size == index_b:
                break
            a = value
            while index_b < size:
                b = each[index_b]
                if a % b == 0 or b % a == 0:
                    inner.append(a)
                    inner.append(b)
                    break
                index_b += 1
        print inner
        result_list.append(max(inner) / min(inner))

    print result_list
    _sum = sum(result_list)
    print _sum
    return _sum


if __name__ == '__main__':
    _input = """5\t1\t9\t5
               7\t5\t3
               2\t4\t6\t8""".strip()

    assert run_it_a([5, 1, 9, 5]) == 8
    assert run_it_a([7, 5, 3]) == 4
    assert run_it_a([2, 4, 6, 8]) == 6
    assert do_it_a(_input) == 18

    _input = """1224	926	1380	688	845	109	118	88	1275	1306	91	796	102	1361	27	995
1928	2097	138	1824	198	117	1532	2000	1478	539	1982	125	1856	139	475	1338
848	202	1116	791	1114	236	183	186	150	1016	1258	84	952	1202	988	866
946	155	210	980	896	875	925	613	209	746	147	170	577	942	475	850
1500	322	43	95	74	210	1817	1631	1762	128	181	716	171	1740	145	1123
3074	827	117	2509	161	206	2739	253	2884	248	3307	2760	2239	1676	1137	3055
183	85	143	197	243	72	291	279	99	189	30	101	211	209	77	198
175	149	259	372	140	250	168	142	146	284	273	74	162	112	78	29
169	578	97	589	473	317	123	102	445	217	144	398	510	464	247	109
3291	216	185	1214	167	495	1859	194	1030	3456	2021	1622	3511	222	3534	1580
2066	2418	2324	93	1073	82	102	538	1552	962	91	836	1628	2154	2144	1378
149	963	1242	849	726	1158	164	1134	658	161	1148	336	826	1303	811	178
3421	1404	2360	2643	3186	3352	1112	171	168	177	146	1945	319	185	2927	2289
543	462	111	459	107	353	2006	116	2528	56	2436	1539	1770	125	2697	2432
1356	208	5013	4231	193	169	3152	2543	4430	4070	4031	145	4433	4187	4394	1754
5278	113	4427	569	5167	175	192	3903	155	1051	4121	5140	2328	203	5653	3233"""

    do_it_a(_input)

    #_input = """5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5"""

    do_it_b(_input)
