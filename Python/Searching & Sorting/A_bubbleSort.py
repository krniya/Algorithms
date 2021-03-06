# O(n ^ 2) | O(1)
def bubbleSort(arr):
    isSorted = False
    count = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1 - count):
            if arr[i] > arr[i+1]:
                swap(i, i + 1, arr)
                isSorted = False
        count += 1
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


print(bubbleSort([3, 1, 5, 7, 8, 12, 2, 9, 15, 11]))
