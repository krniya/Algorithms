from typing import List


def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    def helper(x):
        if x < 0: return 0
        res = 0
        l, curr = 0, 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr > x:
                curr -= nums[l]
                l += 1
            res += r - l + 1
        return res
    return helper(goal) - helper(goal-1)