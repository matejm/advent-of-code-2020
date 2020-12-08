import sys

commands = []
executed = []

for line in sys.stdin:
    line = line.strip().split()
    commands.append((line[0], int(line[1])))
    executed.append(0)

i = 0
acc = 0

while True:
    c, n = commands[i]

    executed[i] += 1

    if executed[i] > 1:
        print('First star: ', acc)
        break

    if c == 'acc':
        acc += n
        i += 1
    elif c == 'nop':
        i += 1
    elif c == 'jmp':
        i += n


for j in range(len(commands)):
    # change command
    new_commands = commands[:]
    executed = [0 for i in range(len(commands))]

    c, n = new_commands[j]

    if c == 'acc':
        continue
    elif c == 'nop':
        c = 'jmp'
    elif c == 'jmp':
        c = 'nop'

    new_commands[j] = (c, n)

    i = 0
    acc = 0

    while i < len(commands):
        c, n = new_commands[i]

        executed[i] += 1

        if executed[i] > 100:
            # Probably infinite loop
            break

        if c == 'acc':
            acc += n
            i += 1
        elif c == 'nop':
            i += 1
        elif c == 'jmp':
            i += n

    if i >= len(commands):
        # success
        print('Second star:', acc)
        break