def uniquePaths(m,n):
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j - 1] + dp[j]
    return dp[-1] if m and n else 0

print (uniquePaths(7,3))
