from functools import cache


def uniquePaths1(m,n):
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j - 1] + dp[j]
    return dp[-1] if m and n else 0


def uniquePaths2(m,n, me={}):
        key = str(m) + "," + str(n)
        if key in me:
            return me[key]
        if m == 0 or n ==0:
            return 0
        if m==1 and n==1:
            return 1
        me[key]= uniquePaths2(m-1,n,me) + uniquePaths2(m,n-1,me)
        return me[key]

def uniquePaths3(m,n):
        @cache
        def dfs(i,j):
            if i < 0 or j < 0:
                return 0
            if i ==0 and j== 0:
                return 1
            return dfs(i-1,j) + dfs(i,j-1)
        return dfs(m-1,n-1)

def uniquePaths4(m,n):
        if n < m:
            n,m=m,n
        dp = [1] * m
        for i in range(1,n):
            ndp = [1] * m
            for j in range(1,m):
                ndp[j] = ndp[j-1] + dp[j]
            dp = ndp
        return dp[-1]

print (uniquePaths4(3,7))
