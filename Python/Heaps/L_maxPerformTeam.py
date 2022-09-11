import heapq


def maxPerformance(n: int, speed, efficiency, k: int) -> int:
        eng = [[e, s] for s, e in zip(speed, efficiency)]
        eng.sort(reverse = True)
        minHeap = []
        res = speed = 0
        mod = (10 ** 9) + 7
        for eff, spd in eng:
            if len(minHeap) == k:
                speed -= heapq.heappop(minHeap)
            speed += spd
            res = max(res, speed * eff)
            heapq.heappush(minHeap, spd)
        return res % mod

print(maxPerformance(3, [2,8,2], [2,7,1], 2))