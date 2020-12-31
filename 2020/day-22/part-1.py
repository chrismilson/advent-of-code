from collections import deque
import re


def calculateWinningScore(deck1, deck2):
    p1, p2 = deque(deck1), deque(deck2)
    if not p1:
        return sum(i * v for i, v in enumerate(reversed(p2), 1))

    while p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c2 > c1:
            c1, c2 = c2, c1
            p1, p2 = p2, p1
        p1.append(c1)
        p1.append(c2)

    return sum(i * v for i, v in enumerate(reversed(p1), 1))


playerRegex = re.compile(r"^Player (\d+):$")
cardRegex = re.compile(r"^(\d+)$")

if __name__ == "__main__":
    decks = {}

    with open('./decks.txt') as f:
        for line in f:
            if (match := playerRegex.match(line)):
                player = match.groups()[0]
                decks[player] = []
                while (match := cardRegex.match(f.readline())):
                    decks[player].append(int(match.groups()[0]))

    assert(len(decks) == 2)
    deck1, deck2 = decks.values()
    result = calculateWinningScore(deck1, deck2)
    print(result)
