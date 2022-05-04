def isMatch1(s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]

# O(n) space
def isMatch(s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        dp = [False]*(np+1)
           
        for si in range(ns+1):
            new_dp = [si == 0] + [False]*np
            for pi in range(1, np+1):
                if si>0 and p[pi-1] in [s[si-1], '?']:
                    new_dp[pi] = dp[pi-1]
                elif p[pi-1] == '*':
                    new_dp[pi] = dp[pi-1] or dp[pi] or new_dp[pi-1]
            dp = new_dp

        return dp[-1]

print(isMatch("abcde","a*d?"))