from typing import List


def rotatetedSortedSearch(nums: List[int], tar: int) -> int:
    if nums is None:
        return -1
    low, high = 0, len(nums)
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == tar:
            return mid
        if nums[low] < nums[mid]:
            if nums[low] <= tar <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= tar <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
