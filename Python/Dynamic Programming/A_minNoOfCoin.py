# O(nd) | O(n)
def minNoOfCoin(n, denoms):
    noOfCoin = [float("inf") for amount in range(n+1)]
    noOfCoin[0] = 0
    for denom in denoms:
        for amount in range(len(noOfCoin)):
            if denom <= amount:
                noOfCoin[amount] = min(noOfCoin[amount], 1 + noOfCoin[amount - denom])
    return noOfCoin[n] if noOfCoin[n] != float("inf") else -1


print(minNoOfCoin(11,[1,2,5]))
