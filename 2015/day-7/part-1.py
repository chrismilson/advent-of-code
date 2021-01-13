from functools import lru_cache
import re

instructionRegex = re.compile(r"^(.+) -> (\w+)$")
aliasRegex = re.compile(r"^(\w+)$")
binRegex = re.compile(r"^(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+)$")
uniRegex = re.compile(r"^NOT (\w+)$")
OPS = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "LSHIFT": lambda a, b: a << b,
    "RSHIFT": lambda a, b: a >> b
}


def solve(instructions, target: str) -> int:
    @lru_cache(None)
    def rec(target):
        if target.isdigit():
            return int(target)
        if target not in instructions:
            raise ValueError(
                f"There is no instruction for the id \"{target}\"")

        task = instructions[target]
        if (match := aliasRegex.match(task)):
            alias = match.groups()[0]
            return rec(alias)
        if (match := binRegex.match(task)):
            a, op, b = match.groups()
            return OPS[op](rec(a), rec(b))
        if (match := uniRegex.match(task)):
            inv = match.groups()[0]
            return ~rec(inv)

        raise ValueError(f"Unidentified instruction: {task}")
    return rec(target)


if __name__ == "__main__":
    instructions = {}

    with open("./wire-kit.txt") as f:
        for line in f:
            if (match := instructionRegex.match(line)):
                op, result = match.groups()
                instructions[result] = op.strip()

    result = solve(instructions, "a")
    print(result)
