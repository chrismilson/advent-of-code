def countUniqueHouses(directions):
    delta = {
        c: d for c, d in zip("^v<>", [
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ])
    }

    unique = set([(0, 0)])
    x = y = 0
    for c in directions:
        dx, dy = delta[c]
        x += dx
        y += dy
        unique.add((x, y))

    return len(unique)


if __name__ == "__main__":
    with open("./directions.txt") as f:
        directions = list(f.read().strip())

    result = countUniqueHouses(directions)
    print(result)
