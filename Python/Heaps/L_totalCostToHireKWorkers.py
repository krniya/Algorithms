import heapq


def totalCost(costs, k: int, candidates: int) -> int:
        leftBatch = costs[:candidates]
        rightBatch = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(leftBatch)
        heapq.heapify(rightBatch)
        leftPointer, rightPointer = candidates, len(costs) - candidates - 1
        totalcost = 0
        for _ in range(k):
            if not rightBatch or (leftBatch and leftBatch[0] <= rightBatch[0]):
                totalcost += heapq.heappop(leftBatch)
                if leftPointer <= rightPointer:
                    heapq.heappush(leftBatch, costs[leftPointer])
                    leftPointer += 1
            else:
                totalcost += heapq.heappop(rightBatch)
                if leftPointer <= rightPointer:
                    heapq.heappush(rightBatch, costs[rightPointer])
                    rightPointer -= 1
        return totalcost


print(totalCost([1,2,4,1],3, 3))