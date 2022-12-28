import heapq
import math

def minStoneSum(piles, k: int) -> int:
        piles = [ -p for p in piles ]
        heapq.heapify(piles)
        while k:
            stone = -1 * heapq.heappop(piles)
            heapq.heappush(piles, -1 * math.ceil(stone / 2))
            k-=1
        return sum(piles) * -1

print(minStoneSum([5,4,9], 2))