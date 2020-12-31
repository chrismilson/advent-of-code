from typing import List, Tuple
import re


def avoidLoop(commands: List[Tuple[str, int]]) -> int:
    n = len(commands)
    seen = [False] * n

    i = acc = 0

    while not seen[i]:
        op, arg = commands[i]
        seen[i] = True
        if op == 'acc':
            acc += arg
            i += 1
        elif op == 'jmp':
            i += arg
        elif op == 'nop':
            i += 1
        else:
            raise ValueError(f"The operation \"{op}\" is not defined")

    return acc


commandRegex = re.compile(r'^(acc|jmp|nop) ([+-]\d+)$')

if __name__ == "__main__":
    commands = []

    with open('./boot-script.txt') as f:
        for op, arg in map(lambda x: commandRegex.match(x).groups(), f):
            commands.append((op, int(arg)))

    result = avoidLoop(commands)
    print(result)
