# Time: O(log(n)) | Space: O(log(n))
def binarySearch(arr, tar):
    return binarySearchHelper(arr, tar, 0, len(arr) - 1)

def binarySearchHelper(arr, tar, l, r):
    if l > r:
        return -1
    middle = (l + r) // 2
    potMatch = arr[middle]
    if tar == potMatch:
        return middle
    elif tar < potMatch:
        return binarySearchHelper(arr, tar, l, middle - 1)
    else:
        return binarySearchHelper(arr, tar, middle + 1, r)

# Time: O(log(n)) | Space: O(1)
def binarySearch1(arr, tar):
    l = 0
    r = len(arr) - 1
    while l <= r:
        middle = (l + r) // 2
        potMatch = arr[middle]
        if tar == potMatch:
            return middle
        elif tar < potMatch:
            r = middle - 1
        else:
            l = middle + 1
    return -1

x = [1,2,3,4,5,6,7,8,9]
print(binarySearch1(x,7))

