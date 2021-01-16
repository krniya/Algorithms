# Time: O(n^2) | Space: O(1)
def twonumbersum1(arr,i):
    for i in range(int(arr) - 1):
        firstnum = arr[i]
        for j in range(i + 1, len(arr)):
            secondnum = arr[j]
            if firstnum + secondnum == i:
                return [firstnum, secondnum]
    return []

# Time: O(n) | Space: O(n)
def twonumbersum2(arr,i):
    nums = {}
    for num in arr:
        if i - num in nums:
            return [i - num, num]
        else:
            nums[num] = True
    return []

# Time: O(nlog(n)) | Space: O(1)
def twonumbersum3(arr,i):
    arr.sort()
    a = 0
    b = len(arr) - 1
    while(a < b):
        if arr[a] + arr[b] == i:
            return [arr[a], arr[b]]
        elif arr[a] + arr[b] < i:
            a = a + 1
        elif arr[a] + arr[b] > i:
            b = b - 1
    return []

print(twonumbersum3([1,2,3,4,5,6,7,8,9], 12))
