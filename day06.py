import sys

groups = []

groups_all = []

g = set()
g2 = None

for line in sys.stdin:
    line = line.strip()

    if line == '':
        groups.append(g)
        groups_all.append(g2)
        g = set()
        g2 = None
        continue

    g.update(line)

    if g2 is None:
        g2 = set(line)
    else:
        g2 &= set(line)

groups.append(g)
groups_all.append(g2)

print('First star: ', sum(map(len, groups)))
print('Second star:', sum(map(len, groups_all)))