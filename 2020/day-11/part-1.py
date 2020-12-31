OCCUPIED = 1
EMPTY = 0
FLOOR = 5


def generate(seats):
    n = len(seats)
    m = len(seats[0])
    nextSeats = [x[:] for x in [[0] * m] * n]

    for i in range(n):
        for j in range(m):
            for i1 in range(i-1, i+2):
                for j1 in range(j-1, j+2):
                    if i1 == i and j1 == j:
                        continue
                    if 0 <= i1 < n and 0 <= j1 < m and seats[i1][j1] != FLOOR:
                        nextSeats[i][j] += seats[i1][j1]

    for i in range(n):
        for j in range(m):
            if seats[i][j] == OCCUPIED and nextSeats[i][j] >= 4:
                nextSeats[i][j] = EMPTY
            elif seats[i][j] == EMPTY and nextSeats[i][j] == 0:
                nextSeats[i][j] = OCCUPIED
            else:
                nextSeats[i][j] = seats[i][j]

    return nextSeats


if __name__ == "__main__":
    seats = []
    with open('./seating-plan.txt') as f:
        for line in f:
            row = []
            for square in line.strip():
                if square == '.':
                    row.append(FLOOR)
                elif square == 'L':
                    row.append(EMPTY)
            seats.append(row)

    while True:
        nextSeats = generate(seats)
        if all(
            all(a == b for a, b in zip(*rows))
            for rows in zip(seats, nextSeats)
        ):
            result = sum(
                seat == OCCUPIED
                for row in seats
                for seat in row
            )
            break
        seats = nextSeats

    print(result)
