from collections import defaultdict
from typing import List


def maxSubarrayLength(nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res