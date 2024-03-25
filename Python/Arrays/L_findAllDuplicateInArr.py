from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    result = []
    for n in nums:
        n = abs(n)
        if nums[n-1] < 0:
            result.append(n)
        nums[n-1] = -nums[n-1]
    return result