import re


def validateYear(value: str, lo: int, hi: int):
    return value.isdigit() and lo <= int(value) <= hi


def validateBirthYear(value: str):
    return validateYear(value, 1920, 2002)


def validateIssueYear(value: str):
    return validateYear(value, 2010, 2020)


def validateExpirationYear(value: str):
    return validateYear(value, 2020, 2030)


hgtRegex = re.compile(r'^(\d+)(in|cm)$')


def validateHeight(value: str):
    match = hgtRegex.match(value)
    if match == None:
        return False
    num, unit = match.groups()
    if unit == 'cm':
        return 150 <= int(num) <= 193
    elif unit == 'in':
        return 59 <= int(num) <= 76


hclRegex = re.compile(r'^#[0-9a-f]{6}$')


def validateHairColor(value: str):
    return hclRegex.match(value) != None


eclRegex = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')


def validateEyeColor(value: str):
    return eclRegex.match(value) != None


validate = {
    'byr': validateBirthYear,
    'iyr': validateIssueYear,
    'eyr': validateExpirationYear,
    'hgt': validateHeight,
    'hcl': validateHairColor,
    'ecl': validateEyeColor,
    'pid': lambda x: len(x) == 9 and x.isdigit()
}


def isValidPassport(candidate):
    return all(
        field in candidate and validate[field](candidate[field])
        for field in validate
    )


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
