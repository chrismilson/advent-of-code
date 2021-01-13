from itertools import islice
from typing import List


def lookAndSay(sequence: List[int]):
    prev = sequence[0]
    count = 1
    result = []

    for v in islice(sequence, 1, None):
        if v == prev:
            count += 1
        else:
            result.append(count)
            result.append(prev)
            prev = v
            count = 1
    result.append(count)
    result.append(prev)
    return result


if __name__ == "__main__":
    initial = "1113222113"
    generations = 50

    sequence = list(map(int, initial))
    for _ in range(generations):
        sequence = lookAndSay(sequence)
    result = len(sequence)
    print(result)
