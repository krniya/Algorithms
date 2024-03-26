from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)):  # delete those useless elements
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
        nums[nums[i] % n] += n
    for i in range(1, len(nums)):
        if nums[i]//n == 0:
            return i
    return n


def firstMissingPositive1(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        if nums[i] < 0:
            nums[i] = 0
    for i in range(n):
        val = abs(nums[i])
        if 1 <= val <= n:
            if nums[val-1] > 0:
                nums[val-1] *= -1
            elif nums[val-1] == 0:
                nums[val-1] *= -1 * (n + 1)
    for i in range(1, n + 1):
        if nums[i-1] > 0:
            return i
    return n + 1
        

print(firstMissingPositive([3,4,-1,1]))
