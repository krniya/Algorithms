from typing import List


def searchInsertPosition(nums: List[int], tar: int) -> int:
    if not nums:
        return -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < tar:
            low = mid + 1
        else:
            if nums[mid] == tar and nums[mid - 1] != tar:
                return mid
            else:
                high = mid - 1
    return low


print(searchInsertPosition([1, 2, 3, 4, 4, 6, 7, 8], 4))
