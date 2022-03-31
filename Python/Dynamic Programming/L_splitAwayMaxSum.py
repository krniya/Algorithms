def splitArray(nums, m):
    minResult, maxResult = 0,0
    for num in nums:
        maxResult += num
        if num > minResult:
            minResult = num
    finalResult = float('inf')
    while minResult <= maxResult:
        mid = (minResult + maxResult) // 2
        if isPossibility(mid, nums, m):
            finalResult = mid
            maxResult = mid-1
        else:
            minResult = mid+1
    return finalResult

def isPossibility(x, nums, m):
    numSubarrays = 1
    subarraySum = 0
    for num in nums:
        if (num + subarraySum) <= x:
            subarraySum += num
        else:
            numSubarrays += 1
            subarraySum = num
    return (numSubarrays <= m)