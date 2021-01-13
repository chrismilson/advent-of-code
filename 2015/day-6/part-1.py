from typing import List, Tuple
import re


def countOn(instructions: List[Tuple[str, Tuple[int, int], Tuple[int, int]]]) -> int:
    """
    Counts the number of lights on after executing the instructions.
    """
    state = [x[:] for x in [[0] * 1000] * 1000]
    tasks = {
        "on": lambda x: 1,
        "off": lambda x: 0,
        "toggle": lambda x: 1 - x
    }

    for task, (x1, y1), (x2, y2) in instructions:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                state[x][y] = tasks[task](state[x][y])
    
    return sum(sum(row) for row in state)


instructionRegex = re.compile(
    r"^(?:turn )?(on|off|toggle) (\d+,\d+) through (\d+,\d+)$")

if __name__ == "__main__":
    instructions = []

    with open('./instructions.txt') as f:
        for line in f:
            if (match := instructionRegex.match(line)):
                task, x1y1, x2y2 = match.groups()
                instructions.append(
                    (task, *map(lambda xy: tuple(map(int, xy.split(','))), (x1y1, x2y2))))

    result = countOn(instructions)
    print(result)
