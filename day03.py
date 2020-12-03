import sys

m = []
for line in sys.stdin:
    m.append(line.strip())

width = len(m[0])

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1

for dx, dy in slopes:
    x = 0
    y = 0
    trees = 0

    while y < len(m):
        if m[y][x % width] == '#':
            trees += 1

        x += dx
        y += dy

    if dx == 3 and dy == 1:
        print('First star:', trees)

    total *= trees

print('Second star:', total)