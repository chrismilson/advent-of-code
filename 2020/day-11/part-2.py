from collections import defaultdict

OCCUPIED = 1
EMPTY = 0
FLOOR = -1


def findSteadyState(seats):
    # A list of index pairs of neighbors for each seat.
    neighbors = defaultdict(list)
    n = len(seats)
    m = len(seats[0])

    for i in range(n):
        for j in range(m):
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == dj == 0:
                        continue
                    i1 = i + di
                    j1 = j + dj
                    while 0 <= i1 < n and 0 <= j1 < m and seats[i1][j1] == FLOOR:
                        i1 += di
                        j1 += dj
                    if 0 <= i1 < n and 0 <= j1 < m:
                        neighbors[i, j].append((i1, j1))

    # Non zero to ensure start
    changing = True
    while changing:
        changing = False
        neighborCount = [x[:] for x in [[0] * m] * n]

        for i in range(n):
            for j in range(m):
                for i1, j1 in neighbors[i, j]:
                    neighborCount[i][j] += seats[i1][j1] == OCCUPIED

        for i in range(n):
            for j in range(m):
                if seats[i][j] == OCCUPIED and neighborCount[i][j] >= 5:
                    changing = True
                    seats[i][j] = EMPTY
                elif seats[i][j] == EMPTY and neighborCount[i][j] == 0:
                    changing = True
                    seats[i][j] = OCCUPIED
    
    return seats

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

    findSteadyState(seats)

    result = sum(
        seat == OCCUPIED
        for row in seats
        for seat in row
    )

    print(result)
