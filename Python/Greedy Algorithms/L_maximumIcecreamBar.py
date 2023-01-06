from typing import List
import heapq

def maxIceCream(costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        total = 0
        while costs and coins:
            price = heapq.heappop(costs)
            if price > coins:
                return total
            coins -= price
            total += 1
        return total