from typing import List
import math

def minimumRounds(tasks: List[int]) -> int:
        counter = {}
        res = 0
        for t in tasks:
            counter[t] = counter.get(t,  0) + 1
        for task, count in counter.items():
            if count == 1:
                return -1
            else:
                res += math.ceil(count / 3)
        return res