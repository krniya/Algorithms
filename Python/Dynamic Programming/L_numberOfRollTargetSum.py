def numRollsToTarget(d: int, f: int, target: int) -> int:
        if target < d or target > d * f:
            return 0
			
        if target > d * (1 + f) / 2:
            target = d * (1 + f) - target
        dp = [0] * (target + 1) 
        for i in range(1, min(f, target) + 1):
            dp[i] = 1

        for i in range(2, d + 1):
            new_dp = [0] * (target + 1)
            for j in range(i, min(target, i * f) + 1):
                new_dp[j] = new_dp[j - 1] + dp[j - 1]
                if j - 1 > f:
                    new_dp[j] -= dp[j - f - 1]
            dp = new_dp

        return dp[target] % (10 ** 9 + 7)