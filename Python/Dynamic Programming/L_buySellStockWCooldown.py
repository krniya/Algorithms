def maxProfit(prices) -> int:
        cache = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in cache:
                return cache[(i,buying)]
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cache[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cache[(i, buying)] = max(sell, cooldown)
            return cache[(i, buying)]
        return dfs(0, True)

def maxProfit(prices) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0, 0] for i in range(n+1)]
        dp[1][1] = 0 - prices[0] 
        for i in range(2, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])    #don't buy or sell
            dp[i][1] = max(dp[i-2][0] - prices[i-1], dp[i-1][1])     # buy on i-th day or don't buy
        return max(dp[-1])