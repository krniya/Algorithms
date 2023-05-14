import math
from functools import lru_cache


def maxScore(nums) -> int:
        @lru_cache(None)
        def gcd(x, y):
            return math.gcd(x, y)

        @lru_cache(None)
        def dp(op, mask):
            if op == n + 1:  # Reach to n operations
                return 0

            ans = 0
            for i in range(m):
                if (mask >> i) & 1: continue  # If nums[i] is used -> Skip
                for j in range(i + 1, m):
                    if (mask >> j) & 1: continue  # If nums[j] is used -> Skip
                    newMask = (1 << i) | (1 << j) | mask  # Mark nums[i] and nums[j] as used!
                    score = op * gcd(nums[i], nums[j]) + dp(op + 1, newMask)
                    ans = max(ans, score)
            return ans

        m = len(nums)
        n = m // 2
        return dp(1, 0)