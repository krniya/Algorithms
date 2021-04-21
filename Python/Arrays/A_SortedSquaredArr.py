def sortedSquaredArr(arr):
    sortedSquared = [0 for _ in arr]
    smallValIdx = 0
    largeValIdx = len(arr) - 1
    for idx in reversed(range(len(arr))):
        smallVal = arr[smallValIdx]
        largeVal = arr[largeValIdx]
        if abs(smallVal) > abs(largeVal):
            sortedSquared[idx] = smallVal * smallVal
            smallValIdx += 1
        else:
            sortedSquared[idx] = largeVal * largeVal
            largeValIdx -= 1
    return sortedSquared
