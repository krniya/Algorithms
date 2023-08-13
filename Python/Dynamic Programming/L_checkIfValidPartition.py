from typing import List


def validPartition(A: List[int]) -> bool:
        n = len(A)
        dp = [False, False, False, True]
        for i in range(n):
            dp[i % 4] = False
            if i - 1 >= 0 and A[i] == A[i-1]:
                dp[i % 4] |= dp[(i - 2) % 4]
            if i - 2 >= 0 and A[i] == A[i-1] == A[i-2]:
                dp[i % 4] |= dp[(i - 3) % 4]
            if i - 2 >= 0 and A[i] == A[i-1] + 1 == A[i-2] + 2:
                dp[i % 4] |= dp[(i - 3) % 4]
        return dp[(n - 1) % 4]