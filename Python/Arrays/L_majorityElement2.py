from collections import defaultdict
from typing import List


def majorityElement(nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            
            if len(count) < 3:
                continue
            
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count
            
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res
                