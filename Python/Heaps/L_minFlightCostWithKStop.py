def findCheapestPrice(n: int, flights, src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k+1):
            tempPrice = prices.copy()
            for src, dest, cost in flights:
                if prices[src] == float("inf"):
                    continue
                if prices[src] + cost < tempPrice[dest]:
                    tempPrice[dest] = prices[src] + cost
            prices = tempPrice
        return prices[dst] if prices[dst] != float("inf") else -1