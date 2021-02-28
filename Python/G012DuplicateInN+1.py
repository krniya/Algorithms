from typing import List


def findDuplicate(nums: List[int]) -> int:
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    # Find the "entrance" to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return hare


print(findDuplicate([1, 2, 3, 4, 5, 6, 3, 7]))
