allAnswers = 'abcdefghijklmnopqrstuvwxyz'

if __name__ == "__main__":
    group = set(allAnswers)
    result = 0

    with open('./customs-decleration.txt') as f:
        for line in f:
            if line == '\n':
                result += len(group)
                group = set(allAnswers)
            else:
                intersection = set()
                for c in line.strip():
                    if c in group:
                        intersection.add(c)
                group = intersection
    result += len(group)
    print(result)
