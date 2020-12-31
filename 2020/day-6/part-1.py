if __name__ == "__main__":
    group = set()
    result = 0

    with open('./customs-decleration.txt') as f:
        for line in f:
            if line == '\n':
                result += len(group)
                group = set()
            else:
                for c in line.strip():
                    group.add(c)

    print(result)
