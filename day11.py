import sys

l = []

for line in sys.stdin:
    l.append(line.strip())

n = len(l)
m = len(l[0])

original_l = l[:]

anything_changed = True

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


while anything_changed:
    anything_changed = False

    new_l = [list(l[i]) for i in range(n)]

    for y in range(n):
        for x in range(m):
            c = 0
            for dx, dy in dirs:
                if 0 <= x + dx < m and 0 <= y + dy < n and l[y + dy][x + dx] == '#':
                    c += 1

            if c == 0 and new_l[y][x] == 'L':
                new_l[y][x] = '#'
                anything_changed = True
            elif c >= 4 and new_l[y][x] == '#':
                new_l[y][x] = 'L'
                anything_changed = True

    l = new_l

print('First star: ', sum(i.count('#') for i in l))

l = original_l
anything_changed = True

while anything_changed:
    anything_changed = False

    new_l = [list(l[i]) for i in range(n)]

    for y in range(n):
        for x in range(m):
            c = 0
            for dx, dy in dirs:
                t = 1
                while 0 <= x + t * dx < m and 0 <= y + t * dy < n and l[y + t * dy][x + t * dx] == '.':
                    t += 1
                if 0 <= x + t * dx < m and 0 <= y + t * dy < n and l[y + t * dy][x + t * dx] == '#':
                    c += 1

            if c == 0 and new_l[y][x] == 'L':
                new_l[y][x] = '#'
                anything_changed = True
            elif c >= 5 and new_l[y][x] == '#':
                new_l[y][x] = 'L'
                anything_changed = True

    l = new_l

print('Second star: ', sum(i.count('#') for i in l))