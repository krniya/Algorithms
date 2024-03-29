from typing import List


def countSubarrays(nums: List[int], k: int) -> int:
    max_n, max_cnt = max(nums), 0
    res = l = 0
    for r in range(len(nums)):
        if nums[r] == max_n:
            max_cnt += 1
        while max_cnt > k or (l <= r and max_cnt == k and nums[l] != max_n):
            if nums[l] == max_n:
                max_cnt -= 1
            l+=1
        if max_cnt == k:
            res += l + 1
    return res

