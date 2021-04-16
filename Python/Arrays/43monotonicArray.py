# O(n) | O(1)
def isMonotonic(arr):
    if len(arr) <= 2:
        return True
    direction = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i] - arr[i-1]
            continue
        if breakDirection(direction, arr[i-1], arr[i]):
            return False
        return True
    
def breakDirection(direction, previousInt, currentInt):
    diff = currentInt - previousInt
    if diff > 0:
        return diff < 0
    return diff > 0

# O(n) | O(1)
def isMonotonic1(arr):
    isNoneDecreasing = True
    isNoneIncreasing = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            isNoneDecreasing = False
        if arr[i] > arr[i-1]:
            isNoneIncreasing = False
    return isNoneDecreasing or isNoneIncreasing