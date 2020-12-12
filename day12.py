import sys
from math import sin, cos, pi

x, y = 0, 0
direction = (1, 0)

x2, y2 = 0, 0
waypoint = [10, 1]

def change_dir(d, angle):
    s = sin(angle / 180 * pi)
    c = cos(angle / 180 * pi)
    return (d[0] * c - d[1] * s, d[0] * s + d[1] * c)

for line in sys.stdin:
    c, *n = line
    n = int(''.join(n))

    if c == 'N':
        y += n
        waypoint[1] += n
    elif c == 'S':
        y -= n
        waypoint[1] -= n
    elif c == 'E':
        x += n
        waypoint[0] += n
    elif c == 'W':
        x -= n
        waypoint[0] -= n
    elif c == 'F':
        x += direction[0] * n
        y += direction[1] * n
        x2 += waypoint[0] * n
        y2 += waypoint[1] * n
    elif c == 'R':
        direction = change_dir(direction, -n)
        waypoint = list(map(round, change_dir(waypoint, -n)))
    elif c == 'L':
        direction = change_dir(direction, n)
        waypoint = list(map(round, change_dir(waypoint, n)))
    else:
        print('Nothing')

print('First star: ', round(abs(x) + abs(y)))
print('Second star:', abs(x2) + abs(y2))