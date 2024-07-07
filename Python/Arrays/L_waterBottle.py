def numWaterBottles(numBottles: int, numExchange: int) -> int:
    bottle_drinked = 0
    empty = 0
    while numBottles:
        bottle_drinked += numBottles
        empty += numBottles
        numBottles = empty // numExchange
        empty = empty % numExchange
    return bottle_drinked


print(numWaterBottles(9,3))