from typing import List


def generate(board: List[List[List[int]]]):
    # The board may increase in size by 1 in any direction.
    nw = len(board)
    nz = len(board[0])
    ny = len(board[0][0])
    nx = len(board[0][0][0])

    nextBoard = [
        [
            [
                [
                    0 for k in range(nx + 2)
                ] for j in range(ny + 2)
            ] for i in range(nz + 2)
        ] for l in range(nw + 2)
    ]

    for l, space in enumerate(board):
        for i, plane in enumerate(space):
            for j, row in enumerate(plane):
                for k, state in enumerate(row):
                    for l1 in range(l, l+3):
                        for i1 in range(i, i+3):
                            for j1 in range(j, j+3):
                                for k1 in range(k, k+3):
                                    if l1 == l+1 and i1 == i+1 and j1 == j+1 and k1 == k+1:
                                        continue
                                    nextBoard[l1][i1][j1][k1] += state

    for l, space in enumerate(nextBoard):
        for i, plane in enumerate(space):
            for j, row in enumerate(plane):
                for k, count in enumerate(row):
                    prev = 0
                    if 0 < l <= nw:
                        if 0 < i <= nz:
                            if 0 < j <= ny:
                                if 0 < k <= nx:
                                    prev = board[l - 1][i-1][j-1][k-1]
                    if prev:
                        nextBoard[l][i][j][k] = 1 if count in [2, 3] else 0
                    else:
                        nextBoard[l][i][j][k] = 1 if count == 3 else 0

    return nextBoard


if __name__ == "__main__":
    simulate = 6

    board = []
    with open('./initial-slice.txt') as f:
        for line in f:
            row = []
            for c in line.strip():
                row.append(1 if c == '#' else 0)
            board.append(row)
    board = [[board]]

    for i in range(simulate):
        board = generate(board)

    result = 0
    for space in board:
        for plane in space:
            for row in plane:
                result += sum(row)

    print(result)
