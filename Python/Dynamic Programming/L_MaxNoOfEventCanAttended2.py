
from bisect import bisect
from typing import List


def maxValue(A: List[List[int]], K: int) -> int:
        A.sort(key=lambda sev: sev[1])
        # create two dp lists to track maxValues with k-1(dp) and k(dp2) events attended
        # each element in the list means [last_endDay_with_maxValue_so_far, maxValue]
        dp, dp2 = [[0, 0]], [[0, 0]]
        for k in range(K):
            # try to get maxValues with k events
            for s, e, v in A:
                # for each event, find the largest endDay in k-1 list before the event startDay
                i = bisect.bisect(dp, [s]) - 1
                # only append new [endDay, maxValue] to the k list if maxValue is a new max value
                # in this way we can guarantee maxValues only increase in the list, which is the key for bisect above
                if dp[i][1] + v > dp2[-1][1]:
                    dp2.append([e, dp[i][1] + v])
            # assign dp2 as k-1 list and start a new round if k < K
            dp, dp2 = dp2, [[0, 0]]
        # return the maxValue of the last element as it's guaranteed to be the max value overall
        return dp[-1][-1]