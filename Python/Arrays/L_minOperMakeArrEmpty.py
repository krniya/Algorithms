from typing import List


def min_Operation(nums: List[int]) -> int:
    nums_count = {}
    for number in nums:
        nums_count[number] = 1 + nums_count.get(number, 0)
    min_operations = 0
    for value in nums_count.values():
        if value == 1:
            return -1
        min_operations += value // 3
        if value % 3:
            min_operations += 1
    return min_operations

