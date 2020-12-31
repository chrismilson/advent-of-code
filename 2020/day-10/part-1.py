from collections import Counter

if __name__ == "__main__":
    with open('./joltage-adapters.txt') as f:
        joltages = [0] + list(map(int, f))

    joltages.sort()
    c = Counter(b - a for a, b in zip(joltages, joltages[1:]))
    c[3] += 1
    print(c)
    print(c[1] * c[3])
