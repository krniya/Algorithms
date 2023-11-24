from typing import List


def maxCoins(self, piles: List[int]) -> int:
    piles.sort()
    n = len(piles)
    res = 0
    for i in range(n//3,n,2):
        res += piles[i]
    return res

