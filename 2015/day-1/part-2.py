if __name__ == "__main__":
    with open("./instructions.txt") as f:
        instructions = f.read().strip()

    floor = 0
    for i, c in enumerate(instructions, 1):
        floor += (c == '(') - (c == ')')
        if floor == -1:
            result = i
            break

    print(result)
