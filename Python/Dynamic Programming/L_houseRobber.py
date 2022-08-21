from functools import cache


def rob(nums) -> int:
        n = len(nums)
        @cache
        def robs(i):
            if i >= n:
                return 0
            return nums[i] + max(robs(i+2), robs(i+3))
        return max(robs(0), robs(1))

def rob(nums) -> int:
        if len(nums) == 1:
            return nums[0]
        first = nums[0]
        second = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            curr = max(second, first + nums[i])
            first = second
            second = curr
        return second