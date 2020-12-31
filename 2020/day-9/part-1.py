from typing import List
from collections import deque


def twoSum(nums: List[int], target: int) -> bool:
    """
    Checks whether there is a pair of nums that sum to the target.
    """
    seen = set()

    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False


def firstInvalid(nums: List[int]) -> int:
    """
    Returns the first number that is not the sum of any pair of numbers in the
    25 before it.
    """
    q = deque(nums[:25])

    for num in nums[25:]:
        if not twoSum(q, num):
            return num
        q.popleft()
        q.append(num)
    return -1


if __name__ == "__main__":
    with open('./encoded-data.txt') as f:
        numbers = list(map(int, f))

    result = firstInvalid(numbers)
    print(result)
