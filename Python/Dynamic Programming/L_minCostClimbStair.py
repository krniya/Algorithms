def minCostClimbingStairs(cost) -> int:
        N = len(cost)
        dp = [0 for _ in range(N + 1)]
        
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            
        return dp[-1]

def minCostClimbingStairs(cost) -> int:
        if len(cost) < 3:
            return min(cost)
        first = cost[0]
        second = cost[1]
        for n in cost[2:]:
            curr = n + min(first,second)
            first = second
            second = curr
        return min(first,second)

def minCostClimbingStairs(cost) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])