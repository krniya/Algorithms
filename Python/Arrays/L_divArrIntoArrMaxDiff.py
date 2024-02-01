from typing import List


def divideArray(nums, k):
    size = len(nums)
    if size % 3 != 0:
        return []

    nums.sort()

    result = []
    group_index = 0
    for i in range(0, size, 3):
        if i + 2 < size and nums[i + 2] - nums[i] <= k:
            result.append([nums[i], nums[i + 1], nums[i + 2]])
            group_index += 1
        else:
            return []
    return result


def divideArray1(nums: List[int], k: int) -> List[List[int]]:
        # Sort the input array
        nums.sort()
        res = []

        # Iterate over the sorted array in steps of 3
        for i in range(0, len(nums), 3):
            # Check if there are at least 3 elements remaining
            if i + 2 < len(nums):
                # If the difference between the maximum and minimum elements in the subarray is greater than k, return an empty list
                if nums[i + 2] - nums[i] > k:
                    return []
                # Append the current subarray to the result
                res.append([nums[i], nums[i + 1], nums[i + 2]])

        return res