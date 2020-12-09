import sys
from collections import deque, defaultdict

N = 25

l = []

for line in sys.stdin:
    n = int(line.strip())

    if len(l) < 25:
        l.append(n)
        continue

    cool = False
    d = len(l) - 1

    for i in range(25):
        for j in range(i):
            if l[d - i] + l[d - j] == n and l[d - i] != l[d - j]:
                cool = True
                break
        if cool:
            break

    if not cool:
        print('First star: ', n)
        break

    l.append(n)


for i in range(len(l)):
    s = l[i]
    j = 1
    while s < n:
        s += l[i + j]
        j += 1

    if s == n:
        minimal = min(l[i : i + j])
        maximal = max(l[i : i + j])

        print('Second star:', minimal + maximal)
        break

