import re


def calculateError(rules, tickets):
    result = 0
    for ticket in tickets:
        for num in ticket:
            if not any(
                lo <= num <= hi
                for rule in rules
                for lo, hi in rules[rule]
            ):
                result += num
    return result


# Captures the name and the list of ranges.
ruleRegex = re.compile(r'^([^:]+):(.*)$')
# Captures the list of numbers
ticketRegex = re.compile(r'^((?:\d+,)*\d+)$')


if __name__ == "__main__":
    rules = {}
    myTicket = []
    nearbyTickets = []

    with open('./ticket-info.txt') as f:
        # Read the rules
        while (match := ruleRegex.match(f.readline())):
            ruleName, rangesStr = match.groups()

            def getRange(rng):
                lo, hi = map(int, rng.strip().split('-'))

                return (lo, hi)

            rules[ruleName] = list(map(
                getRange,
                rangesStr.strip().split('or')
            ))

        for line in f:
            if (match := ticketRegex.match(line)):
                numList = match.groups()[0]
                myTicket = list(map(int, numList.split(',')))
                break

        for line in f:
            if (match := ticketRegex.match(line)):
                numList = match.groups()[0]
                nearbyTickets.append(list(map(int, numList.split(','))))

    result = calculateError(rules, nearbyTickets)
    print(result)
