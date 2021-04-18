# O(n^2) | O(1)
def selectionSort(arr):
    currIndex = 0
    while currIndex < len(arr) - 1:
        smallestIdx = currIndex
        for i in range(currIndex + 1, len(arr)):
            if arr[smallestIdx] > arr[i]:
                smallestIdx = i
        swap(currIndex, smallestIdx, arr)
        currIndex += 1
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


print(selectionSort([3,5,2,45,6,76,34,65,235,54,63]))


