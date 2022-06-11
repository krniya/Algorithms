from bisect import bisect
from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        for s in spells:
            factor = (success + s - 1) // s
            pairs.append(len(potions) - bisect.bisect_left(potions, factor))
        return pairs