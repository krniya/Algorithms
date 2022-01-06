def longestCommonSequence(n,m,s1,s2):
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if s1[i] == s2[j]:
                ans = 1 + dp[i+1][j+1]
            else:
                a1 = dp[i+1][j]
                a2 = dp[i][j+1]
                ans = max(a1,a2)
            dp[i][j] = ans
    return dp[0][0]

print(longestCommonSequence(6,6,"ABCDGH", "AEDFHR"))