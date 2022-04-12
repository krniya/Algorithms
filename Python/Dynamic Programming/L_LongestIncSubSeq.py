def longestIncSubSeq(nums):
    def binarySearch(sub, val):
        lo, hi = 0, len(sub)-1
        while(lo <= hi):
            mid = lo + (hi - lo)//2
            if sub[mid] < val:
                lo = mid + 1
            elif val < sub[mid]:
                hi = mid - 1
            else:
                return mid
        return lo
        
    sub = []
    for val in nums:
        pos = binarySearch(sub, val)
        if pos == len(sub):
            sub.append(val)
        else:
            sub[pos] = val
    return len(sub)


def lengthOfLIS(nums) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        return max(LIS)

def lengthOfLIS1(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

print(lengthOfLIS1([10,9,2,5,3,7,101,18]))