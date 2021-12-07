def maxProfit(prices):
    mins = maxs = prices[0]
    op = 0
    for share in prices[1:]:
        if share < mins:
            if op < maxs - mins:
                op = maxs - mins
            mins = share
            maxs = float("-inf")
        elif share > maxs:
            maxs = share
    if op > maxs - mins and op > 0:
        return op
    elif maxs-mins > 0:
        return maxs -mins
    else:
        return 0

print(maxProfit([3,2,6,5,0,3]))