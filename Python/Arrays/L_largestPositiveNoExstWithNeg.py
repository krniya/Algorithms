from typing import List


def findMaxK(nums: List[int]) -> int:
    n_set = set(nums)
    max_num = -1
    for n in n_set:
        if n * -1 in n_set:
            max_num = max(max_num, abs(n))
    return max_num