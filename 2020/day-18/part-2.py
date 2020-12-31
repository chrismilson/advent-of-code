def calculate(expression: str) -> int:
    def evaluate(s: int, e: int) -> int:
        """
        Evaluates the sub expression: expression[s:e].
        """
        depth = 0
        subExprStart = 0
        mult = 1
        plus = 0
        num = 0

        for i in range(s, e):
            c = expression[i]
            if c == ' ':
                continue

            if c == '(':
                if depth == 0:
                    subExprStart = i + 1
                depth += 1
            elif c == ')':
                depth -= c == ")"

                if depth == 0:
                    num = evaluate(subExprStart, i)
            elif depth > 0:
                continue
            elif c.isdigit():
                num = 10 * num + int(c)
            else:
                # the character c is an operator. We must calculate the previous
                # operation, and then we can move on.
                plus += num
                num = 0
                if c == "*":
                    # We have fininshed the current sum
                    mult *= plus
                    plus = 0

        # finish the last operation
        return mult * (plus + num)

    return evaluate(0, len(expression))


if __name__ == "__main__":
    with open("./maths-homework.txt") as f:
        expressions = [line.strip() for line in f]

    result = sum(calculate(expression) for expression in expressions)

    print(result)
