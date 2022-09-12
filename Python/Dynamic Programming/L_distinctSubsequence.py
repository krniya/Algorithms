def numDistinct(s: str, t: str) -> int:
        cache = {}
        
        def dp(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i] == t[j]:
                cache[(i,j)] = dp(i+1,j+1) + dp(i+1,j)
            else:
                cache[(i,j)] = dp(i+1,j)
            return cache[(i,j)]
        return dp(0,0)