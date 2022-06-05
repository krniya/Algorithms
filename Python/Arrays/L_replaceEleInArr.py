from typing import List


def arrayChange(nums: List[int], operations: List[List[int]]) -> List[int]:
        lookup = {}
        for i,n in enumerate(nums):
            lookup[n]=i
        for x,y in operations:
            idx = lookup[x]
            nums[idx] = y
            lookup[y] = idx
            del lookup[x]
        return nums
