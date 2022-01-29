def houseRobberII(nums):
    def rob(nums, a, j):
        first = nums[a]
        second = max(nums[a], nums[a+1])
        for i in range(a + 2, j):
            curr = max(second, first + nums[i])
            first = second
            second = curr
        return second
    if len(nums) < 3:
        return max(nums)
    else:
        left = rob(nums, 1, len(nums))
        right = rob(nums, 0, len(nums) - 1)
        return max( left, right)

print(houseRobberII([1,2,3,4,5,6]))