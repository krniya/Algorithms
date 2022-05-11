def countVowelStrings(n: int) -> int:
        return ((n + 1) * (n + 2) *(n + 3) *(n + 4)) // 24

def countVowelStrings1(n):
        seen = {}
        def dp(n, k):
            if k == 1 or n == 1: return k
            if (n, k) in seen:
                return seen[n, k]
            seen[n, k] = sum(dp(n - 1, k) for k in range(1, k + 1))
            return seen[n, k]
        return dp(n, 5)

def countVowelStrings2(n):
        dp = [0] + [1] * 5
        for _ in range(1, n + 1):
            for k in range(1, 6):
                dp[k] += dp[k - 1]
        return dp[5]

print(countVowelStrings2(3))

