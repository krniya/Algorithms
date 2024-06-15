def minIncrementForUnique(nums):
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                ans += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return ans
        