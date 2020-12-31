from typing import List, Tuple
import re


class LoopError(ValueError):
    pass


def runWithMistake(commands):
    """
    There is a single nop or jmp instruction that should be a jmp or nop
    instruction respectively. This program will find the mistake and return the
    intended final value of the accumulator.
    """
    n = len(commands)
    seen = [False] * n
    changed = -1

    # k is the number of remaining changes we can make.
    def bt(i, k):
        nonlocal changed
        if not 0 <= i <= n:
            raise ValueError("Segmentation fault")
        if i == n:
            return 0
        if seen[i]:
            raise ValueError("Infinite loop detected.")

        op, arg = commands[i]
        seen[i] = True

        try:
            if op == 'acc':
                return bt(i + 1, k) + arg
            if op == 'jmp':
                if k > 0:
                    # Lets try to change this command.
                    # Assuming this was intended to be a nop...
                    try:
                        changed = i
                        return bt(i + 1, k - 1)
                    except ValueError:
                        pass
                return bt(i + arg, k)
            if op == 'nop':
                if k > 0:
                    try:
                        changed = i
                        return bt(i + arg, k - 1)
                    except ValueError:
                        pass
                return bt(i + 1, k)
        except ValueError as err:
            seen[i] = False
            # re-raise after erasing
            raise err

    return bt(0, 1)


commandRegex = re.compile(r'^(acc|jmp|nop) ([+-]\d+)$')

if __name__ == "__main__":
    commands = []

    with open('./boot-script.txt') as f:
        for op, arg in map(lambda x: commandRegex.match(x).groups(), f):
            commands.append((op, int(arg)))

    result = runWithMistake(commands)
    print(result)
