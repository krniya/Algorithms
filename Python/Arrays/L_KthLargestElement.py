import heapq
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

def findKthLargest(nums, k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        L, M = len(left), len(mid)
        if k <= L:
            return findKthLargest(left, k)
        elif k > L + M:
            return findKthLargest(right, k - L - M)
        else:
            return mid[0]


def findKthLargest(nums, k: int) -> int:
        heap = []
        size = 0
        for num in nums:
            heapq.heappush(heap, num)
            size += 1
            if size > k:
                heapq.heappop(heap)
                size -= 1
        return heapq.heappop(heap)

print(findKthLargest([3,2,5,1,4,7,6], 3))
