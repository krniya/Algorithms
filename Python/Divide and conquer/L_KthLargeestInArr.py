from random import random


def findKthLargest(nums, k) -> int:
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