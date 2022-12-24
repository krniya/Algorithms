from functools import cache


def numTilings(n: int) -> int:
    @cache
    def solve(i, previous_gap):
            if i > n: return 0
            if i == n: return not previous_gap
            if previous_gap:
                return solve(i+1, False) + solve(i+1, True)
            return solve(i+1, False) + solve(i+2, False) + 2*solve(i+2, True)
    return solve(0, False) % 1_000_000_007


def numTilings(n: int) -> int:
        dp = [[0, 0] for _ in range(3)]
        dp[1], dp[2] = [1, 1], [2, 2]
        for i in range(3, n+1):
            dp[i%3][0] = dp[(i-1)%3][0] + dp[(i-2)%3][0] + 2*dp[(i-2)%3][1]
            dp[i%3][1] = dp[(i-1)%3][0] + dp[(i-1)%3][1]
        return dp[n%3][0] % 1_000_000_007