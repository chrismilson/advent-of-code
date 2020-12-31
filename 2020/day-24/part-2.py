from collections import Counter
from typing import List
from itertools import chain
import re


def simulateMovesThenCountBlack(tiles: List[str], numMoves: int) -> int:
    # Since our coordinates are inside a 2-d hexagonal "grid", I will use the
    # basis (ne, e) and then define each move as a sum of these basis elements.
    basis = {
        'ne': (1, 0),
        'e': (0, 1),
        'se': (-1, 1),
        'sw': (-1, 0),
        'w': (0, -1),
        'nw': (1, -1)
    }

    # counts how many times each tile has been flipped.
    state = Counter()

    for tile in tiles:
        x, y = 0, 0
        for move in tile:
            dx, dy = basis[move]
            x += dx
            y += dy
        state[x, y] += 1

    black = set()
    for xy in state:
        if state[xy] & 1:
            black.add(xy)

    for _ in range(numMoves):
        sumNeighbors = Counter()

        for x, y in black:
            for dx, dy in basis.values():
                sumNeighbors[x + dx, y + dy] += 1

        newBlack = set()
        for xy in black:
            if sumNeighbors[xy] in [1, 2]:
                newBlack.add(xy)

        for xy in sumNeighbors:
            if xy in black:
                continue
            if sumNeighbors[xy] == 2:
                newBlack.add(xy)

        black = newBlack

    return len(black)


moveSepRegex = re.compile(r"(ne|e|se|sw|w|nw)")

if __name__ == "__main__":
    tiles = []
    with open("tiles.txt") as f:
        # with open("example.txt") as f:
        for line in f:
            tiles.append(list(filter(bool, moveSepRegex.split(line.strip()))))

    result = simulateMovesThenCountBlack(tiles, 100)
    print(result)
