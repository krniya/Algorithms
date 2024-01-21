
from functools import cache
from typing import List


def rob(nums) -> int:
        n = len(nums)
        @cache
        def robs(i):
            if i >= n:
                return 0
            return nums[i] + max(robs(i+2), robs(i+3))
        return max(robs(0), robs(1))

def rob1(nums) -> int:
        if len(nums) == 1:
            return nums[0]
        first = nums[0]
        second = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            curr = max(second, first + nums[i])
            first = second
            second = curr
        return second
    
def rob2(nums: List[int]) -> int:
    prev1, prev2 = 0, 0
    for i in nums:
        prev1, prev2 = prev2, max(prev1+i, prev2)
    return prev2