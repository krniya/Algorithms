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