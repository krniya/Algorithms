from typing import Counter, List


def findWinners(matches):
        lost = {}
        people = set()
        for i, j in matches:
            people.add(i)
            people.add(j)
        for i in people:
            lost[i] = 0
        for i, j in matches:
            lost[j] += 1
        zero = []
        one = []
        for i in people:
            if lost[i] == 0:
                zero.append(i)
            elif lost[i] == 1:
                one.append(i)
        zero.sort()
        one.sort()
        return [zero, one]
    
    
    

def findWinners(m: List[List[int]]) -> List[List[int]]:
    return [sorted({w for w,_ in m}-{*(q:=Counter(l for _,l in m))}),sorted(l for l in q if q[l]==1)]