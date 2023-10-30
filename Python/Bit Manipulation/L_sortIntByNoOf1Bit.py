from typing import List


def sortByBits(arr: List[int]) -> List[int]:
    arr.sort(key= lambda x: (bin(x).count('1'),x))
    return arr
        