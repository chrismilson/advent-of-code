if __name__ == "__main__":
    with open("./instructions.txt") as f:
        instructions = f.read().strip()

    result = 0
    for c in instructions:
        result += (c == '(') - (c == ')')

    print(result)
