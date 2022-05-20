#O(nd) | O(n)
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]

def change(amt, coins) -> int:
        dp = {}
        def dfs(i,a):
            if a == amt:
                return 1
            if a > amt:
                return 0
            if i == len(coins):
                return 0
            if (i,a) in dp:
                return dp[(i,a)]
            dp[(i,a)] = dfs(i,a+coins[i]) + dfs(i+1, a)
            return dp[(i,a)]
        return dfs(0,0)


print(numberOfWaysToMakeChange(10, [1, 2, 3, 4]))
