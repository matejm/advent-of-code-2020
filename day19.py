import sys
import itertools

rules_fl = True

rules = {}

to_validate = []

for line in sys.stdin:
    line = line.strip()

    if line == '':
        rules_fl = False
        continue

    if rules_fl:
        a, b = line.split(': ')
        rules[int(a)] = b
    else:
        to_validate.append(line)


def create_rule(k):
    val = rules[k]
    if isinstance(val, list):
        return val
    if val[0] == '"':
        rules[k] = [val.replace('"', '')]
        return [val.replace('"', '')]

    result = []
    options = val.split(' | ')
    
    for option in options:
        values = map(int, option.split())
        values = [create_rule(v) for v in values]
        values = list(map(lambda x: ''.join(x), itertools.product(*values)))
        result += values

    rules[k] = result
    return result

for k in rules:
    if rules[k][0] == '"' or rules[k][0].isnumeric():
        create_rule(k)

rules_0 = set(rules[0])
c = 0

for message in to_validate:
    if message in rules_0:
        c += 1

print('First star: ', c)

# we see that
# 0: 8 11
# 8: 42+
# 11: 42+ 31+, same number of 42s and 11s
# therefore
# 0: at least 2 matches if 42 and ends with 31
# furthermore, we see, that all valid messages in rules for 42 have length 8
# same for all message in 31

c = 0

rules_42 = set(rules[42])
rules_31 = set(rules[31])

N = 8

for message in to_validate:
    if len(message) < 3 * N or len(message) % N != 0:
        continue

    b = True
    for i in range(0, len(message) - N, N):
        m = message[i : i + N]
        if m not in rules_42:
            b = False
            break

    if b:
        if message[-N : ] in rules_31:
            c += 1
        continue

    l = len(message) // N
    t = i // N
    if not (t - 1 >= l - t) or not (t >= 2):
        continue

    b = True
    for j in range(i, len(message), N):
        m = message[j : j + N]
        if m not in rules_31:
            b = False
            break
    if not b:
        continue

    c += 1

print('Second star: ', c)
