from collections import defaultdict
from typing import List, Tuple
import re


def shortestRoundTrip(distances: List[Tuple[str, str, int]]) -> int:
    """
    Calculates the shortest round trip through the graph represented by
    distances.
    """
    graph = defaultdict(dict)
    for a, b, dist in distances:
        graph[a][b] = dist
        graph[b][a] = dist

    been = {place: False for place in graph}
    result = 0

    def bt(dist, prev):
        nonlocal result
        if all(been.values()):
            result = max(result, dist)
            return

        for place in graph:
            if been[place]:
                continue
            been[place] = True
            bt(dist + graph[prev][place], place)
            been[place] = False

    for place in graph:
        been[place] = True
        bt(0, place)
        been[place] = False

    return result


distanceRegex = re.compile(r"^(\w+) to (\w+) = (\d+)$")

if __name__ == "__main__":
    distances = []

    with open('./distances.txt') as f:
        for line in f:
            if (match := distanceRegex.match(line)):
                a, b, dist = match.groups()
                distances.append((a, b, int(dist)))

    result = shortestRoundTrip(distances)
    print(result)
