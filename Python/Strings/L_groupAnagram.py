from collections import defaultdict
from typing import List


def getSignature(s: str) -> str:
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1

    result = []
    for i in range(26):
        if count[i] != 0:
            result.extend([chr(i + ord('a')), str(count[i])])

    return ''.join(result)

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = []
    groups = defaultdict(list)

    for s in strs:
        groups[getSignature(s)].append(s)

    result.extend(groups.values())

    return result