import re

middleRegex = re.compile(r"(.)(?<=.\1)")


def isNice(name: str) -> bool:
    seen = {}
    h = 0
    h += ord(name[0]) - ord("a")

    for i in range(1, len(name)):
        h = h * 26 + ord(name[i]) - ord("a")
        h %= 26 * 26
        if h in seen:
            if seen[h] < i - 1:
                break
        else:
            seen[h] = i
    else:
        return False

    for a, b in zip(name, name[2:]):
        if a == b:
            break
    else:
        return False
    return True


if __name__ == "__main__":
    names = []
    with open("./santas-list.txt") as f:
        for line in f:
            names.append(line.strip())

    # # examples
    # print(isNice("aaa"))
    # print(isNice("xyxy"))
    # print(isNice("abcdefeghi"))
    # print(isNice("xxyxx"))

    result = sum(map(isNice, names))
    print(result)
