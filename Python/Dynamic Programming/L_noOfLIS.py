from typing import List


def findNumberOfLIS(nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)] # length, cnt
        max_length = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] = dp[i][1] + dp[j][1]
            max_length = max(max_length, dp[i][0])
        res = 0
        for idx, (length, cnt) in enumerate(dp):
            if length == max_length:
                res += cnt
        return res