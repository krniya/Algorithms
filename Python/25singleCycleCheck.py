# O(n) | O(1)
def hasSingleCycle(arr):
    visited = 0
    currIndex = 0
    while visited < len(arr):
        if visited > 0 and currIndex == 0:
            return False
        visited += 1
        currIndex = getNextIdx(currIndex, arr)
    return currIndex == 0

def getNextIdx(currIdx, arr):
    jump = arr[currIdx]
    nextIdx = (currIdx + jump) % len(arr)
    return nextIdx if nextIdx >= 0 else nextIdx + len(arr)

print(hasSingleCycle([2,3,-1,-3,-1]))

