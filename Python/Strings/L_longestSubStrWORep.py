from typing import List


def longestSubString(s: str) -> int:
    res = left = 0
    alreadyHave = set()
    for right, ch in enumerate(s):
        while ch in alreadyHave:
            alreadyHave.remove(s[left])
            left+=1
        alreadyHave.add(ch)
        res = max(res, right - left + 1)
    return res


print(longestSubString("pwwkew"))
