from collections import deque


def countArrangements(adapters):
    adapters.sort()
    n = len(adapters)

    # There is one way to arrange the first adapter.
    q = deque([1])
    s = 1

    # The way to arrange the next adapter will be the sum of the ways to arrange
    # any adapter within 3 jolts of it.
    lo = 0

    for hi in range(1, n):
        while adapters[hi] - adapters[lo] > 3:
            s -= q.popleft()
            lo += 1
        q.append(s)
        s *= 2
    return q[-1]


if __name__ == "__main__":
    with open('./joltage-adapters.txt') as f:
        joltages = [0] + list(map(int, f))

    joltages.sort()
    joltages.append(joltages[-1] + 3)

    c = countArrangements(joltages)
    print(c)
