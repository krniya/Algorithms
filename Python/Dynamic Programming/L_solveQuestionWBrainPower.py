def mostPoints(questions) -> int:
        cache = {}
        def dfs(i):
            if i >= len(questions):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(dfs(i+1), dfs(i+1+questions[i][1]) + questions[i][0])
            return cache[i]
        return dfs(0)


def mostPoints(questions) -> int:
    dp = {}
    for i in range(len(questions) - 1, -1, -1):
        dp[i] = max(dp.get(i+1, 0), questions[i][0] + dp.get(i+1+questions[i][1],0))
    return dp[0]