

import bisect


def longestObstacleCourseAtEachPosition(nums):
        res = []
        dp = [10**8] * (len(nums) + 1)
        for n in nums:
            index = bisect.bisect(dp, n)
            res.append(index + 1)
            dp[index] = n
        return res