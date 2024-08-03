from typing import List


def canBeEqual(target: List[int], arr: List[int]) -> bool:
    cnt = {}
    for n in target:
        cnt[n] = cnt.get(n, 0) + 1
    for n in arr:
        cnt[n] = cnt.get(n, 0) - 1
        if cnt[n] == 0:
            del cnt[n]
    return len(cnt) == 0