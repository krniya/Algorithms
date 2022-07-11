import heapq


def fillCups(amount) -> int:
        pq = [-q for q in amount if q != 0]
        heapq.heapify(pq)
        ret = 0
        while len(pq) > 1:
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)
            first += 1
            second += 1
            ret += 1
            if first:
                heapq.heappush(pq, first)
            if second:
                heapq.heappush(pq, second)

        if pq:
            return ret - pq[0]
        else:
            return ret

print(fillCups([5,4,4]))