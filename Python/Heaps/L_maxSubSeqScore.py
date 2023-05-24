from heapq import heappop, heappush


def maxScore( A, B, k: int) -> int:
        total = res = 0
        h = []
        for a,b in sorted(list(zip(A, B)), key=lambda ab: -ab[1]):
            heappush(h, a)
            total += a
            if len(h) > k:
                total -= heappop(h)
            if len(h) == k:
                res = max(res, total * b)
        return res