import sys

seats = []

for line in sys.stdin:
    line = line.strip()

    row = line[:7].replace('F', '0').replace('B', '1')
    row = int(row, 2)

    col = line[-3:].replace('R', '1').replace('L', '0')
    col = int(col, 2)

    seat_id = row * 8 + col

    seats.append(seat_id)

print('First star: ', max(seats))

seats.sort()

for i in range(len(seats) - 1):
    if seats[i] + 1 < seats[i + 1]:
        print('Second star:', seats[i] + 1)
        break