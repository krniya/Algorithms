from typing import List


def canCross(stones: List[int]) -> bool:
        d = dict((x,set()) for x in stones)
        if stones[1] != 1:
            return False
        d[1].add(1)
        for i in range(len(stones[1:])):
            for j in d[stones[i]]:
                for k in range(j-1, j+2):
                    if k > 0 and stones[i]+k in d:
                        d[stones[i]+k].add(k)
        return d[stones[-1]] != set()