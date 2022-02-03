def longestConsSeq(nums):
    uni = set(nums)
    count=0
    for num in nums:
        if num - 1 not in uni:
            nex = num+1
            while nex in uni:
                nex+=1
            count = max(count, nex - num)
    return count
    