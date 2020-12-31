from functools import lru_cache
from itertools import islice, chain
from collections import deque
import re


def calculateWinningScore(deck1, deck2):
    index = {v: i for i, v in enumerate(chain(deck1, deck2))}
    value = {i: v for i, v in enumerate(chain(deck1, deck2))}
    base = len(deck1 + deck2)

    @lru_cache(None)
    def rec(h1, n1, h2, n2):
        seen = set()
        while n1 and n2:
            if (h1, n1, h2, n2) in seen:
                return True, h1, n1
            seen.add((h1, n1, h2, n2))
            # Pop from the queue.
            (c1, h1), n1 = divmod(h1, base ** (n1 - 1)), n1 - 1
            (c2, h2), n2 = divmod(h2, base ** (n2 - 1)), n2 - 1

            # Determine who wins.
            if value[c1] <= n1 and value[c2] <= n2:
                p1Wins = rec(
                    h1 // (base ** (n1 - value[c1])), value[c1],
                    h2 // (base ** (n2 - value[c2])), value[c2]
                )[0]
            else:
                p1Wins = value[c2] < value[c1]

            # Update based on winner.
            if p1Wins:
                h1 = (h1 * base + c1) * base + c2
                n1 += 2
            else:
                h2 = (h2 * base + c2) * base + c1
                n2 += 2
        if n1 > 0:
            return True, h1, n1
        return False, h2, n2

    h1 = h2 = 0

    for c in deck1:
        h1 = h1 * base + index[c]
    for c in deck2:
        h2 = h2 * base + index[c]

    hWin, nWin = rec(h1, len(deck1), h2, len(deck2))[1:]
    result = 0
    i = 1

    for i in range(1, nWin + 1):
        hWin, c = divmod(hWin, base)
        result += i * value[c]

    return result


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
    result = calculateWinningScore(decks["1"], decks["2"])
    print(result)
