# O(n^2) | O(1)
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            swap(j, j - 1, arr)
            j -= 1
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]



   