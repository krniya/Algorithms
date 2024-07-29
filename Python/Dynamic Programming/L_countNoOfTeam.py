from typing import List


def numTeams(rating: List[int]) -> int:
    n = len(rating)
    count = 0
    
    for j in range(n):
        leftLess = leftGreater = rightLess = rightGreater = 0

        for i in range(j):
            if rating[i] < rating[j]:
                leftLess += 1
            elif rating[i] > rating[j]:
                leftGreater += 1
        
        for k in range(j + 1, n):
            if rating[k] < rating[j]:
                rightLess += 1
            elif rating[k] > rating[j]:
                rightGreater += 1
        
        count += leftLess * rightGreater + leftGreater * rightLess
    
    return count