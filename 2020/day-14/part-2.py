from collections import defaultdict
import re

maskRegex = re.compile(r'^mask = ([X01]{36})$')
memRegex = re.compile(r'^mem\[(\d+)\] = (\d+)$')


def T():
    return defaultdict(T)


def sumAfterInit(program):
    ones = set()
    floating = set()
    memoryTrie = T()

    for command in program:
        maskMatch = maskRegex.match(command)
        if maskMatch:
            mask = maskMatch.groups()[0]
            ones = set()
            floating = set()
            for i, c in enumerate(mask):
                if c == '1':
                    ones.add(i)
                elif c == 'X':
                    floating.add(i)
            continue
        memMatch = memRegex.match(command)
        if memMatch:
            addr, val = memMatch.groups()

            addr = f'{int(addr):#038b}'[2:]

            # We need to modify the address.
            addr = ''.join(
                'X' if i in floating else ('1' if i in ones else c)
                for i, c in enumerate(addr)
            )

            nodes = [memoryTrie]

            for c in addr:
                if c == 'X':
                    nextNodes = []
                    for node in nodes:
                        nextNodes.append(node['0'])
                        nextNodes.append(node['1'])
                    nodes = nextNodes
                else:
                    nodes = [node[c] for node in nodes]

            for node in nodes:
                node['val'] = int(val)

    # Now we want to dfs through the tree and bubble the vals at the bottom back
    # up to the top.
    def sumNodes(node):
        if 'val' in node:
            return node['val']
        return sum(sumNodes(node[child]) for child in node)

    return sumNodes(memoryTrie)


if __name__ == "__main__":
    with open('./initialisation-program.txt') as f:
        program = list(f)

    result = sumAfterInit(program)

    print(result)
