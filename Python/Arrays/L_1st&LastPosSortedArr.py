from typing import List


def firstAndLastPosSortedArr(nums: List[int], tar: int) -> List[int]:
    if not nums:
        return -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == tar:
            left = right = mid
            while nums[left - 1] == tar:
                left -= 1
            while nums[right + 1] == tar:
                right += 1
            return [left, right]
        if nums[mid] < tar:
            low = mid + 1
        else:
            high = mid - 1
    return [-1, -1]


print(firstAndLastPosSortedArr([1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 8], 10))
