# O(n) | O(1)
def firstDuplicateNo(arr):
    for value in arr:
        if arr[abs(value) - 1] < 0:
            return abs(value)
        arr[abs(value) - 1] *= -1
    return -1

print(firstDuplicateNo([1,2,3,4,5,6,4,3]))