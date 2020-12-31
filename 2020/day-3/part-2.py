from typing import List


def treesHit(slope: List[List[bool]], dx, dy) -> int:
    n = len(slope)
    m = len(slope[0])
    x = y = 0
    result = 0

    while y < n:
        result += slope[y][x]
        x = (x + dx) % m
        y = y + dy

    return result


if __name__ == "__main__":
    slope = []
    with open('./slope.txt') as f:
        for row in f:
            slope.append([])
            for c in row:
                if c == '#':
                    slope[-1].append(True)
                elif c == '.':
                    slope[-1].append(False)

    a, b, c, d, e = [
        treesHit(slope, dx, dy)
        for dx, dy in [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
        ]
    ]

    print(a * b * c * d * e)
