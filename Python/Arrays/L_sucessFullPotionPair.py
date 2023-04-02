from bisect import bisect
from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        for s in spells:
            factor = (success + s - 1) // s
            pairs.append(len(potions) - bisect.bisect_left(potions, factor))
        return pairs


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()
        for i in range(n):
            spell = spells[i]
            left = 0
            right = m - 1
            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs[i] = m - left
        return pairs