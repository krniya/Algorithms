from typing import List


def findDuplicate(nums: List[int]) -> int:
    h = t =nums[0]
    while True:
        t =nums[t]
        h = nums[nums[h]]
        if t == h:
            break
    t = nums[0]
    while t != h:
        t = nums[t]
        h = nums[h]
    return t

def findDuplicate1(nums: List[int]) -> int:
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow   