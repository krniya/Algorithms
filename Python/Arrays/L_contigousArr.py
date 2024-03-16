class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0

        for i in range(len(nums)):
            ones_count = 0
            zeros_count = 0

            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeros_count += 1
                else : # nums[i] == 1:
                    ones_count += 1
                
                if ones_count == zeros_count:
                    max_len = max(max_len, j - i + 1)
            
        return max_len 
