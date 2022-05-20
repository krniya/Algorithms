def findTargetSumWays(nums, target) -> int:
        dp = {}
        n = len(nums)
        def backtrack(i,t):
            if i == len(nums):
                return 1 if t == target else 0
            if (i, t) in dp:
                return dp[(i,t)]
            dp[(i,t)] = backtrack(i+1, t + nums[i]) + backtrack(i+1, t - nums[i])
            return dp[(i,t)]
        return backtrack(0,0)
print(findTargetSumWays([1,1,1,1,1],3))