def maxProfit(prices) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit

def maxProfit(prices) -> int:
	
        n = len(prices)
        
        dp = [[-1 for i in range(2)] for i in range(n)]
        
        def dfs(ind,buy,prices):
            if(ind == len(prices)):
                return 0
            if(dp[ind][buy] != -1):
                return dp[ind][buy]
            if(buy):
                profit = max(-prices[ind] + dfs(ind+1,0,prices), 0 + dfs(ind+1,1,prices))
            else:
                profit = max(prices[ind] + dfs(ind+1,1,prices), 0 + dfs(ind+1,0,prices))
            dp[ind][buy] = profit
            return dp[ind][buy]
        
        return dfs(0,1,prices)