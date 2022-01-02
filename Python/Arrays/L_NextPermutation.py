def nextPermutation(nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:
        nums.reverse()
        return
    k = i - 1
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]
    l, r = k+1, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums

def nextPeru(n, arr):
    ind = -1
    for i in range(n-1,0,-1):
        if arr[i]>arr[i-1]:
            ind = i
            break
    if ind == -1:
        return arr[::-1]
    else:
        prev = ind
        for i in range(ind+1, n):
            if arr[i]>arr[ind-1] and arr[i]<=arr[prev]:
                prev = i           
        arr[ind-1], arr[prev] = arr[prev], arr[ind-1]
        arr[ind:] = arr[-1:ind-1:-1]
    return arr

print(nextPermutation([1, 5, 3, 4, 2]))

