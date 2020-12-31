from collections import defaultdict
import re

ruleRegex = re.compile(r'^(\w+ \w+) bags contain ([^.]*).$')
innerRegex = re.compile(r'^(\d+) (\w+ \w+) bags?$')

if __name__ == "__main__":
    graph = defaultdict(list)

    with open('./bag-rules.txt') as f:
        for rule in f:
            outer, inners = ruleRegex.match(rule).groups()
            for inner in inners.split(', '):
                if inner == 'no other bags':
                    continue
                match = innerRegex.match(inner)
                if not match:
                    print(inner)
                    quit()
                count, name = match.groups()
                if int(count) > 0:
                    graph[name].append(outer)

    topSort = []
    seen = set()

    def dfs(bag):
        if bag in seen:
            return
        seen.add(bag)
        for outer in graph[bag]:
            dfs(outer)
        topSort.append(bag)

    dfs('shiny gold')

    print(len(topSort) - 1)
