import sys
def kthSmallest(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        pos = partition(arr, l, r)
        if (pos - l == k - 1):
            return arr[pos]
        if (pos - l > k - 1):
            return kthSmallest(arr, l, pos - 1, k)
        return kthSmallest(arr, pos + 1, r, k - pos + l - 1)
    return sys.maxsize

def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

print(kthSmallest([3,5,7,2,1,4,6],0,6,3))