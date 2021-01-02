from typing import Tuple
import re


def ribbonBudget(box: Tuple[int, int, int]) -> int:
    """
    Calculates the area of paper that the elves need to wrap a present.
    """
    l, w, h = box
    wrap = (l + w + h - max(l, w, h)) * 2
    bow = l * w * h
    return wrap + bow


presentRegex = re.compile(r"^(\d+)x(\d+)x(\d+)$")

if __name__ == "__main__":
    presents = []

    with open("./dimensions.txt") as f:
        for line in f:
            if (match := presentRegex.match(line)):
                presents.append(tuple(map(int, match.groups())))

    result = sum(map(ribbonBudget, presents))

    print(result)
