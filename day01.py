import sys

l = [int(line) for line in sys.stdin]
finished = False

for a in l:
    for b in l:
        if a + b == 2020:
            print(a * b)
            finished = True
            break

    if finished:
        break

finished = False

for a in l:
    for b in l:
        if a == b or a + b > 2020:
            continue

        for c in l:
            if a + b + c == 2020:
                print(a * b * c)
                finished = True
                break
        if finished:
            break
    if finished:
        break
