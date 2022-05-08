def countTexts(pk: str) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (len(pk) + 1)
        dp[0] = 1
        for i in range(1, len(pk) + 1):
            dp[i] = dp[i-1]
            if i >= 2 and pk[i-1] == pk[i-2]:
                dp[i] += dp[i-2]
            if i >= 3 and pk[i-1] == pk[i-2] and pk[i-2] == pk[i-3]:
                dp[i] += dp[i-3]
            if pk[i-1] in ("79"):
                if i >= 4 and pk[i-1] == pk[i-2] and pk[i-2] == pk[i-3] and pk[i-3] == pk[i-4]:
                    dp[i] += dp[i-4]
            dp[i] %= mod
        return dp[-1]