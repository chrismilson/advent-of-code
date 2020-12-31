from typing import List


def twoSum(nums: List[int], target: int):
    """
    Finds two numbers in nums that add to a target.
    """

    seen = set()

    for num in nums:
        if target - num in seen:
            return num, target - num
        seen.add(num)

    raise ValueError(f"There is no pair that adds to {target}")


if __name__ == "__main__":
    # Load the values from file
    with open('./expense-report.txt') as f:
        expenses = list(map(int, f))

    a, b = twoSum(expenses, 2020)

    print(a, b, a * b)
