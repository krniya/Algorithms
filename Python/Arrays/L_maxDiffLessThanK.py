def partitionArray(nums, k) -> int:
        nums.sort()
        ans = 1
        start = nums[0]
        for i in range(1, len(nums)):
            diff = nums[i] - start
            if diff > k:
                ans += 1
                start = nums[i]
        return ans