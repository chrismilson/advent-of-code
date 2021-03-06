from typing import List, Tuple
import re


def distanceFromStart(moves: List[Tuple[str, int]]) -> int:
    x = 0
    y = 0

    # our current heading
    dx = 1
    dy = 0

    for action, value in moves:
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'F':
            x += dx * value
            y += dy * value
        elif action in 'LR':
            if action == 'L':
                value = 360 - value
            # Now action is Right
            if value == 90:
                dx, dy = dy, -dx
            elif value == 180:
                dx, dy = -dx, -dy
            elif value == 270:
                dx, dy = -dy, dx

    return abs(x) + abs(y)


directiveRegex = re.compile(r'^([NSEWLRF])(\d+)$')


if __name__ == "__main__":
    directives = []
    with open('./directions.txt') as f:
        for directive in f:
            op, arg = directiveRegex.match(directive).groups()
            directives.append((op, int(arg)))

    result = distanceFromStart(directives)
    print(result)
