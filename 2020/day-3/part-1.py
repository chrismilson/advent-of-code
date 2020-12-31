from typing import List


def treesHit(slope: List[List[bool]]) -> int:
    x = 0
    n = len(slope[0])
    result = 0
    for row in slope:
        result += row[x]
        x += 3
        x %= n
    return result


if __name__ == "__main__":
    with open('./slope.txt') as f:
        slope = [[c == '#' for c in row.strip()] for row in f]

    trees = treesHit(slope)

    print(trees)
