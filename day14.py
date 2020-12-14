import sys

def apply_mask(number, mask1, mask2):
    return (number & mask1) | mask2

def apply_mask2(number, mask):
    number = f'{number:0>36b}'

    def options(n, m, prefix):
        if n == '':
            return [prefix]
        if m[0] == '0':
            return options(n[1:], m[1:], prefix + n[0])
        elif m[0] == '1':
            return options(n[1:], m[1:], prefix + '1')
        else:
            return options(n[1:], m[1:], prefix + '1') + options(n[1:], m[1:], prefix + '0')

    return options(number, mask, '')


memory = {}
memory2 = {}

for line in sys.stdin:
    if line.startswith('mask'):
        mask = line.split()[-1]
        mask1 = int(''.join('0' if i == '0' else '1' for i in mask), 2)
        mask2 = int(''.join('1' if i == '1' else '0' for i in mask), 2)
        continue

    mem, _, num = line.split()
    num = int(num)
    mem = int(mem[4 : -1])

    memory[mem] = apply_mask(num, mask1, mask2)

    mems = apply_mask2(mem, mask)
    for m in mems:
        memory2[m] = num

print('First star: ', sum(memory.values()))
print('Second star:', sum(memory2.values()))