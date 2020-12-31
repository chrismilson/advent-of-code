import re


def matches(rules, query: str) -> bool:
    """
    Returns True if the query matches rule zero in the given rules.
    """
    regex = re.compile('^' + rulesToRegexString(rules) + '$')

    return regex.match(query) != None


def rulesToRegexString(rules):
    def rec(rule):
        if rule == "8":
            return f"(?:{rec('42')}+)"
        if rule == "11":
            # Needs to have the same number of 42s as 31s
            rule42 = rec('42')
            rule31 = rec('31')
            return '(' + '|'.join(
                rule42 + f'{{{i}}}' + rule31 + f'{{{i}}}'
                for i in range(1, 10)  # MAGIC NUMBER
            ) + ')'
        if not rule in rules:
            return rule
        return '(' + '|'.join(
            ''.join(rec(token) for token in tokens)
            for tokens in rules[rule]
        ) + ')'

    return rec('0')[1:-1]


ruleRegex = re.compile(r'^(\d+):(.*)$')

if __name__ == "__main__":
    rules = {}
    queries = []

    with open('./message-info.txt') as f:
        while (match := ruleRegex.match(f.readline())):
            name, body = match.groups()

            possibilities = []
            for possibility in body.strip().split("|"):
                possibilities.append([
                    token if token.isdigit() else token[1:-1]
                    for token in possibility.strip().split(" ")
                ])

            rules[name] = possibilities

        for line in f:
            line = line.strip()
            if line:
                queries.append(line)

    print(rulesToRegexString(rules))
    result = sum(matches(rules, query) for query in queries)

    print(result)
