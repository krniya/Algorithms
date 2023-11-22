from collections import deque
from typing import List


#! TLE o(mn) time. o(mn) space
def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    n = len(nums)
    maxL = -1
    result = []
    for i in range(n):
        maxL = max(maxL, len(nums[i]))
        j=0
        while i>=0:
            if j < len(nums[i]):
                result.append(nums[i][j])
            i-=1
            j+=1
    for j in range(1,maxL):
        i=n-1
        while i>=0:
            if j < len(nums[i]):
                result.append(nums[i][j])
            i-=1
            j+=1
    return result


def findDiagonalOrder1(nums: List[List[int]]) -> List[int]:
    res = []
    q = deque([(0, 0)])
    
    while q:
        row, col = q.popleft()
        res.append(nums[row][col])

        if col == 0 and row + 1 < len(nums):
            q.append((row + 1, 0))

        if col + 1 < len(nums[row]):
            q.append((row, col + 1))

    return res


print(findDiagonalOrder([[14,12,19,16,9],[13,14,15,8,11],[11,13,1]]))