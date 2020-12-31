from itertools import islice


def numberGame(startingNumbers):
    mem = {}
    i = 0

    for num in startingNumbers[:-1]:
        yield num
        mem[num] = i
        i += 1

    yield startingNumbers[-1]
    prev = startingNumbers[-1]

    while True:
        if prev in mem:
            num = i - mem[prev]
        else:
            num = 0
        mem[prev] = i
        i += 1
        yield num
        prev = num


if __name__ == "__main__":
    with open('./starting-numbers.txt') as f:
        startingNumbers = list(map(int, f))

    n = 30000000
    # The iterator is zero indexed, so we subtract 1.
    result = next(islice(numberGame(startingNumbers), n - 1, None))

    print(result)
