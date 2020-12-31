def isValidPW(i, j, character, password):
    """
    Determines whether the password is valid according to:

    exactly one of the characters at indicies i and j (1-indexed) in password
    must be equal to character.
    """
    return sum(password[x - 1] == character for x in [i, j]) == 1


if __name__ == "__main__":
    inputs = []

    with open('./passwords.txt') as f:
        for policy, pw in map(lambda x: x.split(': '), f):
            countRange, char = policy.split(' ')
            lo, hi = map(int, countRange.split('-'))
            inputs.append([lo, hi, char, pw])

    print(sum(isValidPW(*x) for x in inputs))
