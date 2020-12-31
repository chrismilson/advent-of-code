from collections import defaultdict
from functools import lru_cache
import re

ruleRegex = re.compile(r'^(\w+ \w+) bags contain ([^.]*).$')
innerRegex = re.compile(r'^(\d+) (\w+ \w+) bags?$')

if __name__ == "__main__":
    graph = defaultdict(dict)

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
                    graph[outer][name] = int(count)

    topSort = []
    seen = set()

    @lru_cache(None)
    def dfs(bag):
        return sum(
            graph[bag][contained] * dfs(contained)
            for contained in graph[bag]
        ) + 1

    result = dfs('shiny gold') - 1

    print(result)
