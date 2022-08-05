def combinationSum4(nums, target: int) -> int:
        dp = {}
        dp[0] = [1]

        def search(target):
            if target in dp:
                return dp[target]
            comb_sum = 0
            for num in nums:
                if target > num:
                    comb_sum += search(target - num)
                elif target == num:
                    comb_sum += 1
            dp[target] = comb_sum
            return comb_sum

        return search(target)

def combinationSum4(nums, target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums: 
                num_before = i - num
                if num_before >= 0:
                    dp[i] += dp[num_before]
        return dp[target]