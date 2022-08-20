import collections
import heapq


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


def findCheapestPrice(n: int, flights, src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, K+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1