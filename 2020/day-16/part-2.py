from bisect import bisect_right, bisect_left
import re


def validTicket(rules, ticket):
    return all(
        any(
            lo <= num <= hi
            for rule in rules
            for lo, hi in rules[rule]
        )
        for num in ticket
    )


def findValidOrder(rules, tickets):
    # only keep valid tickets
    n = len(rules)

    allTickets = [[] for _ in range(n)]
    for ticket in tickets:
        if not validTicket(rules, ticket):
            continue
        for i, num in enumerate(ticket):
            j = bisect_right(allTickets[i], num)
            if j == len(allTickets[i]) or allTickets[i][j] != num:
                allTickets[i].insert(j, num)

    ruleNames = [rule for rule in rules]
    # Contains the order of the rules on the tickets
    fieldOrder = []

    def bt(i):
        if i == n:
            return True
        for rule in ruleNames:
            if rule in fieldOrder:
                continue

            # We want to make sure that every number in allTickets[i] fits
            # within at least one range.

            missing = 0
            for lo, hi in rules[rule]:
                j = bisect_left(allTickets[i], lo)
                if j > missing:
                    # The values in allTickets[j:missing] are invalid for this
                    # rule.
                    break
                else:
                    missing = bisect_right(allTickets[i], hi)
            else:
                # The allocation of rule to index i, may be valid.
                fieldOrder.append(rule)
                if bt(i + 1):
                    return True
                fieldOrder.pop()

    if bt(0):
        return fieldOrder
    raise ValueError("There was no valid order.")


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

            rules[ruleName] = sorted(map(
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

    ruleOrder = findValidOrder(rules, [myTicket] + nearbyTickets)
    print(ruleOrder)
    result = 1
    for rule, num in zip(ruleOrder, myTicket):
        if rule.startswith('departure'):
            result *= num

    print(result)
