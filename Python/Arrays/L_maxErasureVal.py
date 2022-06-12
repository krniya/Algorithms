def maximumUniqueSubarray(nums) -> int:
        l,r = 0,0
        res, tsum = 0,0
        visit = set()
        while r < len(nums):
            if nums[r] not in visit:
                tsum+=nums[r]
                res = max(res, tsum)
                visit.add(nums[r])
                r+=1
            else:
                tsum-=nums[l]
                visit.remove(nums[l])
                l+=1
        return res