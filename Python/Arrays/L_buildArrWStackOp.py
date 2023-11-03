from typing import List


def buildArray(target: List[int], n: int) -> List[str]:
    stack = []
    m = len(target)
    currIdx = 0
    for i in range(1,n+1):
        if i == target[currIdx]:
            stack.append("Push")
            currIdx += 1
        else:
            stack.append("Push")
            stack.append("Pop") 
        if currIdx == m:
            break
    return stack


print(buildArray([1,3], 3))