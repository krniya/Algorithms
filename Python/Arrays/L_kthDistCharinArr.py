from typing import List


def kthDistinct(arr: List[str], k: int) -> str:
    counter = {}
    for ch in arr:
        counter[ch] = counter.get(ch, 0) + 1
    for key, val in counter.items():
        if val == 1:
            if k:
                k-=1
            if k==0:
                return key
    return ""

print(kthDistinct(["d","b","c","b","c","a"], 2))