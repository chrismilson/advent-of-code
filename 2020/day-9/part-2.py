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


def findWeakness(nums):
    """
    Finds the encryption weakness in the numbers
    """
    n = len(nums)

    # Find the invalid number.
    invalid = firstInvalid(nums)

    # build the prefix sums for nums
    pre = [0]
    for num in nums:
        pre.append(pre[-1] + num)

    # We want to find two indicies s < e such that pre[e] - pre[s] = invalid and
    # e - s >= 2

    stack = [(0, n)]
    seen = set()

    while stack:
        s, e = stack.pop()
        if (s, e) in seen or e - s < 2 or pre[e] - pre[s] < invalid:
            continue
        # Preserve s and e.
        if pre[e] - pre[s] == invalid:
            break

        seen.add((s, e))

        stack.append((s + 1, e))
        stack.append((s, e - 1))

    M = max(nums[s:e])
    m = min(nums[s:e])

    return M + m


if __name__ == "__main__":
    with open('./encoded-data.txt') as f:
        numbers = list(map(int, f))

    result = findWeakness(numbers)
    print(result)
