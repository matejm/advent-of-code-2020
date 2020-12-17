import copy
import sys

N = 20

state = [[[False for k in range(N)] for j in range(N)] for i in range(N)]

for i, line in enumerate(sys.stdin):
    state[N // 2][N // 2 - 4 + i][N // 2 - 5 : N // 2 - 5 + len(line)] = [True if c == '#' else False for c in line]

starting_state = copy.deepcopy(state)

for _ in range(6):
    new_state = copy.deepcopy(state)

    for i in range(len(state)):
        for j in range(len(state[i])):
            for k in range(len(state[i][j])):
                active = state[i][j][k]
                c = 0

                # all three directions
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        for dk in range(-1, 2):
                            if di == dj == dk == 0:
                                continue
                            if not (0 <= i + di < N and 0 <= j + dj < N and 0 <= k + dk < N):
                                continue

                            c += state[i + di][j + dj][k + dk]

                if active:
                    if c in (2, 3):
                        new_state[i][j][k] = True
                    else:
                        new_state[i][j][k] = False
                else:
                    if c == 3:
                        new_state[i][j][k] = True
                    else:
                        new_state[i][j][k] = False

    state = new_state

print('First star: ', sum(map(lambda l: sum(map(sum, l)), state)))

state = [[[[False for l in range(N)] for k in range(N)] for j in range(N)] for i in range(N)]
state[N // 2] = starting_state

for _ in range(6):
    new_state = copy.deepcopy(state)

    for i in range(len(state)):
        for j in range(len(state[i])):
            for k in range(len(state[i][j])):
                for l in range(len(state[i][j][k])):
                    active = state[i][j][k][l]
                    c = 0

                    # all three directions
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            for dk in range(-1, 2):
                                for dl in range(-1, 2):
                                    if di == dj == dk == dl == 0:
                                        continue
                                    if not (0 <= i + di < N
                                        and 0 <= j + dj < N
                                        and 0 <= k + dk < N
                                        and 0 <= l + dl < N): continue

                                    c += state[i + di][j + dj][k + dk][l + dl]

                    if active:
                        if c in (2, 3):
                            new_state[i][j][k][l] = True
                        else:
                            new_state[i][j][k][l] = False
                    else:
                        if c == 3:
                            new_state[i][j][k][l] = True
                        else:
                            new_state[i][j][k][l] = False

    state = new_state
    print(f'cycle {_ + 1}', sum(map(lambda l: sum(map(lambda m: sum(map(sum, m)), l)), state)))

print('Second star:', sum(map(lambda l: sum(map(lambda m: sum(map(sum, m)), l)), state)))