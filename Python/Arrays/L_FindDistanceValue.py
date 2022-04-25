class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        dist = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1
            else:
                if arr2[j] - arr1[i] > d:
                    i += 1
                    dist += 1
                else:
                    i += 1
        dist += len(arr1) - i
        return dist