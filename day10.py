import sys

l = [0]

for line in sys.stdin:
    n = int(line.strip())
    l.append(n)

l.sort()

l.append(l[-1] + 3)

jolt1 = 0
jolt3 = 0

for i in range(1, len(l)):
    diff = l[i] - l[i - 1]

    if diff == 1:
        jolt1 += 1
    elif diff == 3:
        jolt3 += 1
    elif diff > 3:
        print('Invalid')
        break

print('First star: ', jolt1 * jolt3)

memo = {}

def count(i):
    if i == len(l) - 1:
        return 1

    if memo.get(i, None) is not None:
        return memo[i]

    val = l[i]
    c = 0

    for j in range(i + 1, len(l)):
        if val + 3 < l[j]:
            break
        c += count(j)

    memo[i] = c
    return c

print('Second star:', count(0))