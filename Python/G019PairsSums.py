class Solution:
    def getPairsCount(self, arr, n, k):
        sums = {}
        for i in arr:
            if i not in sums:
                sums[i] = 0
            else:
                sums[i] += 1
        sec = 0
        for i in arr:
            sec += sums[k - i]
        return sums
