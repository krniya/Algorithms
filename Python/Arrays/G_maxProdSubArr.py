def maxProduct(nums):
    curMax, curMin = 1, 1
    res = nums[0]    
    for n in nums:
        vals = (n, n * curMax, n * curMin)
        curMax, curMin = max(vals), min(vals)	
        res = max(res, curMax)        
    return res

print(maxProduct([2, 3, -4, -5, -1, 0]))