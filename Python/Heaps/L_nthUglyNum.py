import heapq


def nthUglyNumber(n: int) -> int:
        N, m, S = [1], 1, set()
        for _ in range(n):
            while m in S: m = heapq.heappop(N)
            S.add(m)
            for i in [2,3,5]: heapq.heappush(N,i*m)
        return m

print(nthUglyNumber(10))