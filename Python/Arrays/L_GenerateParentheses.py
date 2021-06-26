def GenerateParentheses(n):
    dp = [[] for i in range(n + 1)]
    dp[0].append('')
    for i in range(n + 1):
        for j in range(i):
            dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
    return dp[n]


print(GenerateParentheses(3))
