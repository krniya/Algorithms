from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    res = l = 0
    prod = 1
    for r in range(len(nums)):
        prod *= nums[r]
        while l<=r and prod >= k:
            prod = prod // nums[l]
            l += 1
        res += (r - l + 1)
    return res

