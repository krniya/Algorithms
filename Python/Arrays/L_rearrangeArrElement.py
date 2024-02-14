from typing import List


def rearrangeArray(nums: List[int]) -> List[int]:
    v1, v2, ans = [], [], []
    
    for num in nums:
        if num > 0:
            v1.append(num)
        else:
            v2.append(num)
    
    ind1, ind2 = 0, 0
    
    while ind2 < len(nums) // 2:
        ans.append(v1[ind1])
        ind1 += 1
        ans.append(v2[ind2])
        ind2 += 1
    
    return ans