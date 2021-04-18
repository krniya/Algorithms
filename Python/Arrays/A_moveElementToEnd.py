# O(n) | O(1)
def moveToEnd(arr, tar):
    left = 0
    right = len(arr) - 1
    while left < right:
        while left < right and arr[right] == tar:
            right -= 1
        if arr[left] == tar:
                arr[left], arr[right] = arr[right], arr[left]
        left += 1
    return arr

print(moveToEnd([2,1,2,2,2,3,4,2], 2))