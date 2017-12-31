import re


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


DATA = read_input().splitlines()

hasvowels = re.compile(r'.*[aeiou]{1}.*[aeiou]{1}.*[aeiou]{1}.*')
hasapair  = re.compile(r'.*(.)\1.*')
hasgroups = re.compile(r'ab|cd|pq|xy')

hasdpair = re.compile(r'.*(.{2}).*\1.*')
haspairsep = re.compile(r'.*(.).\1.*')

nice1 = 0
nice2 = 0

for line in DATA:
    isnice1 = True
    isnice2 = True

    if not re.search(hasvowels, line): isnice1 = False
    if not re.search(hasapair, line): isnice1 = False
    if re.search(hasgroups, line): isnice1 = False

    if not re.search(hasdpair, line): isnice2 = False
    if not re.search(haspairsep, line): isnice2 = False

    if isnice1: nice1 += 1
    if isnice2: nice2 += 1

print ("Number of part 1 nice lines: "+str(nice1))
print ("Number of part 2 nice lines: "+str(nice2))
