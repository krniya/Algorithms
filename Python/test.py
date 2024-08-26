import math

class Solution:
    """ Helper function to find the
    maximum element in the array"""
    def findMax(self, nums):
        maxi = float('-inf')
        n = len(nums)

        # Find the maximum element
        for i in range(n):
            maxi = max(maxi, nums[i])
        return maxi

    """ Function to calculate total hours
    required at given hourly rate"""
    def calculateTotalHours(self, nums, hourly):
        totalH = 0
        n = len(nums)

        # Calculate total hours required
        for i in range(n):
            totalH += math.ceil(nums[i] / hourly)
        return totalH

    """ Function to find the 
    minimum rate to eat bananas"""
    def minimumRateToEatBananas(self, nums, h):
        # Initialize binary search bounds
        low, high = 1, self.findMax(nums)

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            totalH = self.calculateTotalHours(nums, mid)
            if totalH <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low

if __name__ == "__main__":
    nums = [7, 15, 6, 3]
    h = 8

    # Create an object of the Solution class
    sol = Solution()

    ans = sol.minimumRateToEatBananas(nums, h)

    # Print the result
    print(f"Koko should eat at least {ans} bananas/hr.")
