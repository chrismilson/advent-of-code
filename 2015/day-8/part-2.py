def discrepancy(s: str) -> int:
    """
    Calculates the difference in the number of characters in the code, and the
    number of characters in memory; how many extra characters are needed to
    represent the string in code as opposed to the real string that the code
    represents.
    """

    return sum(c in "\\\"" for c in s) + 2


if __name__ == "__main__":
    strings = []
    with open('./list.txt') as f:
        for line in f:
            strings.append(line.strip())

    result = sum(discrepancy(s) for s in strings)
    print(result)
