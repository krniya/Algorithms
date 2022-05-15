def waysToSplitArray(nums) -> int:
        count, n = 0, len(nums)
        left, right = 0, sum(nums)
        for i in range(n-1):
            left += nums[i]
            right -= nums[i]
            count += (left >= right)
        return count