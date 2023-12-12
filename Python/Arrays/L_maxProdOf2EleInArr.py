from typing import List


def maxProduct(nums: List[int]) -> int:
    res = 0
    cur_max = nums[0]

    for i in range(1, len(nums)):
        res = max(res, (cur_max - 1) * (nums[i] - 1))
        cur_max = max(cur_max, nums[i])

    return res 