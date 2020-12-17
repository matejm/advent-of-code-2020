starting_numbers = list(map(int, input().split(',')))

def f(N):
    last = {}
    numbers = starting_numbers[:]

    for i in range(len(numbers) - 1):
        last[numbers[i]] = i

    i = len(numbers) - 1

    while i < N - 1:
        v = last.get(numbers[-1], None)
        last[numbers[-1]] = i

        if v is None:
            numbers.append(0)
        else:
            numbers.append(i - v)
        i += 1

    return numbers[-1]

print('First star: ', f(2020))
print('Second star:', f(30000000))