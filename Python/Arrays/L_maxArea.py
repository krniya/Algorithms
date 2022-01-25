from re import I


def maxArea(arr):
    l, r = 0, len(arr) - 1
    water = 0
    while l < r:
        water = max(water, min(arr[l], arr[r]) * (r - l))
        if arr[l] < arr[r]:
            l+=1
        else:
            r+=1
    return water