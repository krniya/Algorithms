from typing import List

def subarraysDivByK(nums: List[int], K: int) -> int:
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for a in nums:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res