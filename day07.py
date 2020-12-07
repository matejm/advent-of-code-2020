import sys
from collections import deque, defaultdict

g = defaultdict(list)
g2 = defaultdict(list)

for line in sys.stdin:
    line = line.strip()

    color, rest = line.split(' bags contain ')

    rest = rest.replace('bags', '').replace('bag', '').replace('.', '').split(', ')

    for color2 in rest:
        n, *t = color2.strip().split(' ')
        color2 = ' '.join(t)

        if color2 != 'other':
            n = int(n)
            g[color2].append(color)
            g2[color].append((n, color2))

# First star
q = deque()
q.append('shiny gold')
visited = defaultdict(bool)

count = 0

while q:
    color = q.popleft()

    for c in g[color]:
        if not visited[c]:
            visited[c] = True
            q.append(c)
            count += 1

print('First star: ', count)

# Second star
def dfs(color):
    s = 0
    for n, c in g2[color]:
        s += n * dfs(c) + n
    return s

print('First star: ', dfs('shiny gold'))
