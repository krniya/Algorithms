from typing import List
from collections import defaultdict

def distinctNames(ideas: List[str]) -> int:
        count = defaultdict(set)
        for a in ideas:
            count[a[0]].add(hash(a[1:]))
        res = 0
        for a, seta in count.items():
            for b, setb in count.items():
                if a >= b: continue
                same = len(seta & setb)
                res += (len(seta) - same) * (len(setb) - same)
        return res * 2