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