import sys

count1 = 0
count2 = 0

for line in sys.stdin:
    limits, letter, password = line.split()

    low, high = map(int, limits.split('-'))
    letter = letter[0]

    occurences = password.count(letter)
    
    if low <= occurences <= high:
        count1 += 1

    first = password[low - 1] == letter
    second = password[high - 1] == letter

    if first ^ second:
        count2 += 1

print(count1)
print(count2)