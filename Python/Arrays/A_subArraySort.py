#O(n) | O(1)
def subArraySort(arr):
    minOutofOrder = float("inf")
    maxOutofOrder = float("-inf")
    for i in range(len(arr)):
        num = arr[i]
        if isOutofBound(i, num, arr):
            minOutofOrder = min(minOutofOrder, num)
            maxOutofOrder = max(maxOutofOrder, num)
    if minOutofOrder == float("inf"):
        return [-1, -1]
    subarrLeftIdx = 0
    while minOutofOrder >= arr[subarrLeftIdx]:
        subarrLeftIdx += 1
    subarrRightIdx = len(arr) - 1
    while maxOutofOrder <= arr[subarrRightIdx]:
        subarrRightIdx -= 1
    return [subarrLeftIdx, subarrRightIdx]


def isOutofBound(i, num, arr):
    if i == 0:
        return num > arr[i + 1]
    if i == len(arr) - 1:
        return num < arr[i - 1]
    return num > arr[i + 1] or num < arr[i - 1]


print(subArraySort([1, 2, 3, 5, 8, 9, 11, 6, 7]))
