import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stones.sort()
        while stones:
            s1 = stones.pop()
            if not stones:
                return s1
            s2 = stones.pop()
            if s1 > s2:
                for i in range(len(stones) + 1):
                    if i == len(stones) or stones[i] > s1-s2:
                        stones.insert(i,s1-s2)
                        break
        return 0

def lastStoneWeight(stones) -> int:
        stones = [ -n for n in stones ]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first < second:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])