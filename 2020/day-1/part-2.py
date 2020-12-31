from typing import List


def threeSum(nums: List[int], target: int):
    """
    Returns three numbers in nums whose sum is target.
    """
    nums.sort()
    n = len(nums)

    for i in range(n):
        lo = i + 1
        hi = n - 1

        while lo < hi and (diff := nums[lo] + nums[hi] + nums[i] - target) != 0:
            if diff < 0:
                lo += 1
            else:
                hi -= 1

        if lo < hi:
            return nums[i], nums[lo], nums[hi]

    raise ValueError(f"There were no triples that sum to {target}")


if __name__ == "__main__":
    # Load the values from file
    with open('./expense-report.txt') as f:
        expenses = list(map(int, f))

    a, b, c = threeSum(expenses, 2020)

    print(a, b, c, a * b * c)
