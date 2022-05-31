class NumArray:
    
    def __init__(self, nums):
        self.prefix = nums
        for i in range(len(nums) - 1):
            self.prefix[i+1] += self.prefix[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]
