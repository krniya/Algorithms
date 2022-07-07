def isInterleave(s1: str, s2: str, s3: str) -> bool:
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [True for _ in range(c+1)] 
        for j in range(1, c+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, r+1):
            dp[0] = (dp[0] and s1[i-1] == s3[i-1])
            for j in range(1, c+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1]


def isInterleave(s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def dfs(i,j):
            if i==len(s1) and j==len(s2):
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            if i<len(s1) and s1[i] == s3[i+j] and dfs(i+1,j):
                return True
            if j<len(s2) and s2[j] == s3[i+j] and dfs(i,j+1):
                return True
            dp[(i,j)] = False
            return False
        return dfs(0,0)