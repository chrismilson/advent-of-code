import re

maskRegex = re.compile(r'^mask = ([X01]{36})$')
memRegex = re.compile(r'^mem\[(\d+)\] = (\d+)$')


def sumAfterInit(program):
    oneMask = 0
    zeroMask = 0
    memory = {}
    for command in program:
        maskMatch = maskRegex.match(command)
        if maskMatch:
            mask = maskMatch.groups()[0]
            oneMask = 0
            zeroMask = 0
            for c in mask:
                oneMask = (oneMask << 1) | (c == '1')
                zeroMask = (zeroMask << 1) | (c == '0')
            continue
        memMatch = memRegex.match(command)
        if memMatch:
            addr, val = memMatch.groups()
            memory[int(addr)] = (int(val) | oneMask) & ~zeroMask

    return sum(memory.values())


if __name__ == "__main__":
    with open('./initialisation-program.txt') as f:
        program = list(f)

    result = sumAfterInit(program)

    print(result)
