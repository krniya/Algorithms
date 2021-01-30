def firstAndLastOccur(arr, tar):
    idx = bSearch(arr, tar)
    if idx == -1:
        return [-1, -1]
    i = idx-1 if arr[idx-1] == tar else idx
    j = idx+1 if arr[idx+1] == tar else idx
    while arr[i-1] == tar or arr[j+1] == tar:
        if arr[i-1] == tar:
            i -= 1
        if arr[j+1] == tar:
            j += 1
    return [i, j]


def bSearch(arr, tar):
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (l+r) // 2
        if arr[mid] > tar:
            r = mid - 1
        elif arr[mid] < tar:
            l = mid + 1
        else:
            return mid
    return -1


print(firstAndLastOccur([1, 3, 5, 5, 5, 5, 7, 123, 125], 7))
