def nonConstChange(coins):
    coins.sort()
    currChangeCoin = 0
    for coin in coins:
        if coin > currChangeCoin + 1:
            return currChangeCoin + 1
        currChangeCoin += coin
    return currChangeCoin + 1


print(nonConstChange([1, 2, 3, 5, 3, 2, 1, 3,
                      5, 6, 4, 3, 6, 5, 4, 3, 1, 4, 5, 3, 2]))
