# O(n) | O(1)
def hasSingleCycle(arr):
    visited = 0
    currIndex = 0
    while visited < len(arr):
        if visited > 0 and currIndex == 0:
            return False
        visited += 1
        jump = arr[currIndex]
        nextIdx = (currIndex + jump) % len(arr)
        currIndex = nextIdx if nextIdx >= 0 else nextIdx + len(arr)
    return currIndex == 0

print(hasSingleCycle([2,3,-1,-3,-1]))

