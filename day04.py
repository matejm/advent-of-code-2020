import sys

passports = []

current = {}

for line in sys.stdin:
    line = line.strip()
    if line == '':
        if current:
            passports.append(current)
            current = {}
        continue

    for a in line.split():
        k, v = a.split(':')
        current[k] = v


keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

count1 = 0
count2 = 0

for p in passports:
    if len(set(p.keys()).intersection(keys)) == 7:
        count1 += 1

    b = int(p.get('byr', '1'))
    if not (1920 <= b <= 2002):
        continue

    i = int(p.get('iyr', '1'))
    if not (2010 <= i <= 2020):
        continue

    e = int(p.get('eyr', '1'))
    if not (2020 <= e <= 2030):
        continue

    h = p.get('hgt', '')
    if not (
        (h.endswith('cm') and 150 <= int(h[:-2]) <= 193) or
        (h.endswith('in') and 59 <= int(h[:-2]) <= 76)):
        continue

    hc = p.get('hcl', '')
    if not (hc.startswith('#')
            and len(hc) == 7
            and set(hc[1:]).issubset(set('1234567890abcdef'))):
        continue

    ec = p.get('ecl', '')
    if not (ec in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        continue

    pid = p.get('pid', '')
    if not (len(pid) == 9 and pid.isnumeric()):
        continue

    count2 += 1

print('First star: ', count1)
print('Second star:', count2)
