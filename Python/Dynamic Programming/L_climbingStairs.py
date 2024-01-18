def climbStairs(n: int) -> int:
    cache = {}
    def backtrack(n):
        if n in cache:
            return cache[n]
        if n < 2:
            return 1
        cache[n] = backtrack(n-1) + backtrack(n-2)
        return cache[n]
    return backtrack(n)