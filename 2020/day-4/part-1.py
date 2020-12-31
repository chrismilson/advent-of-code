requiredFields = [
    'byr',  # Birth Year
    'iyr',  # Issue Year
    'eyr',  # Expiration Year
    'hgt',  # Height
    'hcl',  # Hair Color
    'ecl',  # Eye Color
    'pid'  # Passport ID
    # 'cid'  # Country ID (not required for valid passports)
]


def isValidPassport(candidate):
    return all(field in candidate for field in requiredFields)


if __name__ == "__main__":
    entry = {}
    entries = []
    with open('./passports.txt') as f:
        for line in f:
            if line == '\n':
                # The previous entry is done.
                entries.append(entry)
                entry = {}
                continue

            for token in line.strip().split(' '):
                key, val = token.split(':')
                entry[key] = val
    entries.append(entry)  # add the final entry

    print(
        '\n'.join(map(lambda x: f'{str(x)}, {isValidPassport(x)}', entries[:10])))
    result = sum(isValidPassport(pp) for pp in entries)

    print(result)
