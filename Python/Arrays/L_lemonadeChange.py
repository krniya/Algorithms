from typing import List


def lemonadeChange(bills: List[int]) -> bool:
    if bills[0] != 5:
        return False
    have = [0,0]
    for bill in bills:
        if bill == 5:
            have[0] += 1
        elif bill == 10:
            if have[0]==0:
                return False
            have[0]-=1
            have[1]+=1
        else:
            if have[0]==0 or (have[1] ==0 and have[0]<3):
                return False
            if have[1]:
                have[1]-=1
                have[0]-=1
            else:
                have[0]-=3
    return True
