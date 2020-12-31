from math import ceil
from itertools import islice


def naturals(start=1):
    i = start
    while True:
        yield i
        i += 1


def intersection(iterA, iterB):
    """
    Iterates over the elements common to both iterators.
    Assumes both iterators are increasing and unending.
    """
    a = next(iterA)
    b = next(iterB)

    while True:
        while a < b:
            a = next(iterA)
        while b < a:
            b = next(iterB)
        if a == b:
            yield a
            b = next(iterB)


def findPerfectTimes(buses):
    """
    Calculates the numbers t such that t = i mod b for all (i, b) in buses.

    If all the b are pairwise coprime, then we can use the chinese remainder
    theorem to construct t.
    """

    t, n = 0, 1

    for i, b in buses:
        # We want t + i = 0 mod b, so we know t = -i mod b
        i *= -1
        # We know i = i mod b and by induction t = i_0 mode b_0 for all
        # previous buses.

        while i != t:
            # by either adding a multiple of b to i or a multiple of n to t, we
            # retain our property for both,
            if i < t:
                # We want to find the smallest k such that i + kb ≥ t.
                # This is equivalent to kb ≥ t - i.
                # So the smallest integer k is ceil((t - i) / b).
                i += b * ceil((t - i) / b)
            else:
                t += n * ceil((i - t) / n)
        # Now t = -i mod b. If we make sure to add only multiples of b, we will
        # keep this property.
        n *= b

    while True:
        yield t
        t += n


if __name__ == "__main__":
    with open('./bus-notes.txt') as f:
        t_0 = int(f.readline())
        buses = list(
            map(
                lambda x: (x[0], int(x[1])),
                filter(
                    lambda x: x[1].isdigit(),
                    enumerate(f.readline().strip().split(','))
                )
            )
        )

    result = next(findPerfectTimes(buses))

    print(result)
