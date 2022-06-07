import heapq

def isPossibleDivide(num, k: int) -> bool:
        if len(num) % k:
            return False
        count = {}
        for n in num:
            count[n] = 1 + count.get(n,0)
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + k):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True