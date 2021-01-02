from typing import Tuple
import re


def paperBudget(box: Tuple[int, int, int]) -> int:
    """
    Calculates the area of paper that the elves need to wrap a present.
    """
    l, w, h = box
    boxArea = 2 * (l * w + l * h + w * h)
    extra = (l * w * h // max(l, w, h))
    return boxArea + extra


presentRegex = re.compile(r"^(\d+)x(\d+)x(\d+)$")

if __name__ == "__main__":
    presents = []

    with open("./dimensions.txt") as f:
        for line in f:
            if (match := presentRegex.match(line)):
                presents.append(tuple(map(int, match.groups())))

    result = sum(map(paperBudget, presents))

    print(result)
