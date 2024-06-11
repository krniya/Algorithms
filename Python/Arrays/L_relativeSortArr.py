from collections import defaultdict
from typing import List


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    count = defaultdict(int)
    for n in arr1:
        count[n] += 1
    res = []
    for n in arr2:
        res += [n] * count[n]
        del count[n]
    remain = []
    for key, val in count.items():
        remain += [key] * val
    remain.sort()
    return res + remain