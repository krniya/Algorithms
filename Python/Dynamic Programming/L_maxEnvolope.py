from bisect import bisect_left
from timeit import timeit


def maxEnvelope(envelopes):
        envelopes.sort()
        n = len(envelopes)
        dp = [1] * n
        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)

def maxEnvelopes(envelopes) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _,height in envelopes:
            left = bisect_left(dp, height)
            if left == len(dp): 
                dp.append(height)
            else: 
                dp[left] = height
        return len(dp)

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
