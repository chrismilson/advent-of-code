import re

badRegex = re.compile(r"(ab|cd|pq|xy)")


def isNice(name: str) -> bool:
    if badRegex.search(name) != None:
        return False

    vowels = {v: 0 for v in "aeiou"}
    doubles = 0

    for i in range(len(name)):
        if name[i] in vowels:
            vowels[name[i]] += 1
        doubles += i > 0 and name[i - 1] == name[i]

    return sum(vowels.values()) >= 3 and doubles > 0


if __name__ == "__main__":
    names = []
    with open("./santas-list.txt") as f:
        for line in f:
            names.append(line.strip())

    # examples
    # print(isNice("jchzalrnumimnmhp"))
    # print(isNice("haegwjzuvuyypxyu"))

    result = sum(map(isNice, names))
    print(result)
