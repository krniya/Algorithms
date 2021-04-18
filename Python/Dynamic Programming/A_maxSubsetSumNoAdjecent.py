# O(n) Time | O(n) Space
def maxSubsetSumNoAdjecent(arr):
    if not len(arr):
        return
    elif len(arr) == 1:
        return arr[0]
    maxSum = arr[:]
    maxSum[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        maxSum[i] = max(maxSum[i - 1], maxSum[i - 2] + arr[i])
    return maxSum[-1]


# O(n) Time | O(1) Space
def maxSubsetSumNoAdjecent1(arr):
    if not len(arr):
        return
    elif len(arr) == 1:
        return arr[0]
    first = arr[0]
    second = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        curr = max(second, first + arr[i])
        first = second
        second = curr
    return second


arr = [4, 5, 3, 54, 32, 34, 21, 12, 15]
print(maxSubsetSumNoAdjecent1(arr))