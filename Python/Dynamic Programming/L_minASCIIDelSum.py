def remains(s, i):
    sum_val = 0
    for j in range(i, len(s)):
        sum_val += ord(s[j])
    return sum_val
    
def dfs(i, j, s1, s2, dp):
    if i == len(s1) and j == len(s2):
        return 0
    if i == len(s1) and j < len(s2):
        return remains(s2, j)
    if j == len(s2) and i < len(s1):
        return remains(s1, i)
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = dfs(i + 1, j + 1, s1, s2, dp)
    else:
        dp[i][j] = min(ord(s1[i]) + dfs(i + 1, j, s1, s2, dp),
                        ord(s2[j]) + dfs(i, j + 1, s1, s2, dp))
    return dp[i][j]

def minimumDeleteSum(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[-1 for _ in range(n2)] for _ in range(n1)]
    return dfs(0, 0, s1, s2, dp)
        