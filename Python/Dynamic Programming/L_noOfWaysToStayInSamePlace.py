def numWays(steps: int, arrLen: int) -> int:
    kMod = 1000000007
    n = min(arrLen, steps // 2 + 1)
    dp = [0] * n
    dp[0] = 1
    while steps > 0:
        newDp = [0] * n
        for i in range(n):
            newDp[i] = dp[i]
            if i - 1 >= 0:
                newDp[i] += dp[i - 1]
            if i + 1 < n:
                newDp[i] += dp[i + 1]
            newDp[i] %= kMod
        dp = newDp
        steps -= 1
    return dp[0]