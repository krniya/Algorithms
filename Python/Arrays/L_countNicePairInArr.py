from typing import List


def countNicePairs(nums: List[int]) -> int:
    res = 0
    count = {}
    mod = 10**9 + 7
    
    for n in nums:
        rev = int(str(n)[::-1])
        cur = count.get(n - rev, 0)
        res += cur
        count[n - rev] = 1 + cur

    return res % mod