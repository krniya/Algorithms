import random


def findKthLargest(nums, k: int) -> int:
        k = len(nums) - k
        def quicksel(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p>k: return quicksel(l,p-1)
            elif p < k: return quicksel(p+1, r)
            else: return nums[p]
        return quicksel(0, len(nums) - 1)

print(findKthLargest([3,2,5,1,4,7,6], 3))
