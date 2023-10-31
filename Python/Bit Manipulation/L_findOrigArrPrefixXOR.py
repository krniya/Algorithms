from typing import List


def findArray(pref: List[int]) -> List[int]:
    res = [0] * len(pref)
    res[0] = pref[0]
    for i in range(1,len(pref)):
        res[i] = pref[i] ^ pref[i-1]
    return res