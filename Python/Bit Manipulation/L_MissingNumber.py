from typing import List


def missingNumber(nums) -> int:
        a = len(nums)
        for i,n in enumerate(nums):
            a ^= i ^ n
        return a


def missingNumber(nums: List[int]) -> int:
        n = len(nums)
    v = [-1] * (n + 1)
    for num in nums:
        v[num] = num
    for i in range(len(v)):
        if v[i] == -1:
            return i
    return 0



print(missingNumber([6,65,54]))