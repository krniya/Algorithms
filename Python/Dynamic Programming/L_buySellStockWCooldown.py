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