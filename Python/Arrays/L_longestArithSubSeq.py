def longestArithSeqLength(nums) -> int:
        hm = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                hm[j,diff] = hm.get((i,diff), 1) + 1
        return max(hm.values())