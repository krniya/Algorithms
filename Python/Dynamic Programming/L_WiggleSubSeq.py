def wiggleMaxLength(nums) -> int:
        pos = 1
        neg = 1
        for i,j in zip(nums, nums[1:]):
            if i > j:
                neg = pos + 1
            elif i < j:
                pos= neg + 1
        return max(pos,neg)