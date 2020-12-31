import re
from math import sqrt


class Tile:
    def __init__(self, tile, name):
        n = len(tile)
        self.name = name
        self._rot = 0
        self._flip = False

        def toNum(side):
            num = 0
            b = 1
            rev = 0
            for x in map(lambda x: x == '#', side):
                num = (num << 1) | x
                rev |= b * x
                b <<= 1
            return (num, rev)

        self.sides = [
            toNum(tile[0][i] for i in range(n)),
            toNum(tile[i][-1] for i in range(n)),
            toNum(tile[-1][i] for i in range(n - 1, -1, -1)),
            toNum(tile[i][0] for i in range(n - 1, -1, -1))
        ]

    def rotate(self, val=1):
        """
        Rotates the tile by 90 degrees val times.
        """
        if self._flip:
            val *= -1
        self._rot = (self._rot + val) % 4

    def flip(self):
        """
        Flips the tile in the y axis
        """
        self._flip = not self._flip

    def get(self, rot=0, flip=0):
        """
        Returns the top side of the tile after a further rotation and possible
        flip.
        """
        if self._flip:
            rot = (4 - rot) % 4

        return self.sides[(self._rot + rot) % 4][flip ^ self._flip]


def arrangeTiles(allTiles):
    """
    Finds the ids of the corner pieces of the full image or rearranged tiles.
    """
    tiles = {tile: Tile(allTiles[tile], tile) for tile in allTiles}

    used = {tile: False for tile in tiles}
    tileIds = list(tiles)
    n = int(sqrt(len(tileIds)))
    if n * n != len(tileIds):
        raise ValueError("There are not enough tiles.")
    result = [x[:] for x in [[None] * n] * n]

    def bt(i):
        if i == n * n:
            return True
        x, y = divmod(i, n)

        for tile in tileIds:
            if used[tile]:
                continue
            used[tile] = True
            result[x][y] = tiles[tile]
            for _ in range(4):
                result[x][y].rotate()
                for __ in range(2):
                    result[x][y].flip()
                    if x > 0:
                        left = result[x - 1][y]
                        if left.get(1) != result[x][y].get(-1, 1):
                            # print("failed left")
                            continue
                    if y > 0:
                        up = result[x][y - 1]
                        if up.get(-2) != result[x][y].get(0, 1):
                            # print("failed up")
                            continue
                    if bt(i + 1):
                        return True
            used[tile] = False

    if bt(0):
        return [[t.name for t in row] for row in result]
    raise ValueError("There is no valid arrangement.")


titleRegex = re.compile(r'^Tile (\d+):$')

if __name__ == "__main__":
    tiles = {}

    with open('./image-tiles.txt') as f:
        # with open('./example.txt') as f:
        for line in f:
            if (match := titleRegex.match(line)):
                idNum = int(match.group(1))

                tiles[idNum] = []

                while (rowStr := f.readline().strip()):
                    tiles[idNum].append(list(rowStr))
    img = arrangeTiles(tiles)
    result = img[0][0] * img[0][-1] * img[-1][0] * img[-1][-1]
    print(result)
