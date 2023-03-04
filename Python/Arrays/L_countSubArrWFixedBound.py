def countSubarrays(nums, minK: int, maxK: int) -> int:
        result = 0
        left_index = right_index = bad_index = -1
        
        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                bad_index = i
            if num == minK:
                left_index = i
            if num == maxK:
                right_index = i
            result += max(0, min(left_index, right_index) - bad_index)
        
        return result