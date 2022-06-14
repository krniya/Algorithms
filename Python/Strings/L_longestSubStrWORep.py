from typing import List


def longestSubString(s: str) -> int:
        i=j=res=0
        seen = set()
        while j<len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i+=1
            seen.add(s[j])
            res = max(res,j-i+1)
            j+=1
        return res


print(longestSubString("pwwkew"))
