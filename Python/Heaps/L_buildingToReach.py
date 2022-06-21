import heapq


def furthestBuilding(building, bricks, ladders):
        heap = []
        for i in range(len(building) - 1):
            d = building[i + 1] - building[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(building) - 1


print(furthestBuilding([4,2,7,6,9,14,12],5,1))