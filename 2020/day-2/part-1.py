def isValidPW(lo, hi, character, password):
    """
    Determines whether the password contains a valid number of occurences of a
    certain character.
    """
    count = sum(c == character for c in password)
    return lo <= count <= hi


if __name__ == "__main__":
    inputs = []

    with open('./passwords.txt') as f:
        for policy, pw in map(lambda x: x.split(': '), f):
            countRange, char = policy.split(' ')
            lo, hi = map(int, countRange.split('-'))
            inputs.append([lo, hi, char, pw])

    print(sum(isValidPW(*x) for x in inputs))
