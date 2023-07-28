from typing import List


def PredictTheWinner(nums: List[int]) -> bool:
        dp = list(nums)
        
        for length in range(2, len(nums)+1):
            for i in range(len(nums)-length+1):
                dp[i] =  max(nums[i]-dp[i+1], nums[i+length-1]-dp[i]);
          
        return dp[0] >= 0;