from functools import reduce
from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

min_start = int(input())
buses = list(map(lambda x: None if x == 'x' else int(x), input().split(',')))

m  = 1e9
min_bus = None

for bus in buses:
    if bus is None:
        continue
    if m > bus - min_start % bus:
        m = bus - min_start % bus
        min_bus = bus

print('First star: ', min_bus * m)

M = 1
t = 0

for bus in buses:
    if bus:
        M *= bus

for i, bus in enumerate(buses):
    if bus is not None:
        y = pow(M // bus, -1, bus)
        t += (-i % bus) * (M // bus) * y

print('Second star:', t % M)