from typing import List

def minDeletionSize(strs: List[str]) -> int:
        res = 0
        for j in range(len(strs[0])):
            for i in range(1,len(strs)):
                if strs[i][j] < strs[i-1][j]:
                    res += 1
                    break
        return res