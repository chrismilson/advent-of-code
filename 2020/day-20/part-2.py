import re
from math import sqrt


class Tile:
    def __init__(self, tile, name):
        self.n = len(tile)
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
            toNum(tile[0][i] for i in range(self.n)),
            toNum(tile[i][-1] for i in range(self.n)),
            toNum(tile[-1][i] for i in range(self.n - 1, -1, -1)),
            toNum(tile[i][0] for i in range(self.n - 1, -1, -1))
        ]

        self._inside = [
            row[:]
            for row in tile
        ]

    def getInside(self):
        if self._rot & 1:
            result = [x[1:-1] for x in self._inside[1:-1]]
        else:
            result = [
                [
                    self._inside[j][i]
                    for j in range(1, self.n - 1)
                ] for i in range(1, self.n - 1)
            ]
        if self._rot in [1, 2]:
            for row in result:
                row.reverse()
            result.reverse()
        if (self._rot + self._flip) & 1:
            result.reverse()
        return result

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


def formImage(allTiles):
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
        insides = [[t.getInside() for t in row] for row in result]
        k = result[0][0].n - 2
        result = []
        for r in range(n * k):
            # We watn to add the rth row to the result
            i, j = divmod(r, k)
            result.append(''.join(''.join(insides[i][t][j]) for t in range(n)))
        return result

    raise ValueError("There is no valid arrangement.")


def countRoughWater(image):
    MONSTER = [
        [c == "#" for c in "                  # "],
        [c == "#" for c in "#    ##    ##    ###"],
        [c == "#" for c in " #  #  #  #  #  #   "],
    ]
    # MAGIC TRANSFORM - will not work for general image
    image = [list(row[::-1]) for row in image[::-1]]
    n = len(image)
    count = 0
    monsters = 0
    for i in range(n):
        for j in range(n):
            count += image[i][j] == '#'
            # Look for a monster.
            if i >= len(MONSTER) and j >= len(MONSTER[0]):
                if all(
                    not MONSTER[-mi-1][-mj-1] or image[i-mi][j-mj] == '#'
                    for mi in range(len(MONSTER))
                    for mj in range(len(MONSTER[0]))
                ):
                    monsters += 1
                    for mi in range(len(MONSTER)):
                        for mj in range(len(MONSTER[0])):
                            if MONSTER[-mi-1][-mj-1]:
                                image[i - mi][j - mj] = "O"
    print('\n'.join(''.join(row) for row in image))
    return sum(sum(c == '#' for c in row) for row in image)


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

    img = formImage(tiles)
    result = countRoughWater(img)

    print(result)
