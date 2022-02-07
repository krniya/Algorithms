# O(n) | O(n)
def spiralTraversal(arr):
    result = []
    startRow, endRow = 0, len(arr) - 1
    startCol, endCol = 0, len(arr[0]) - 1
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(arr[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            result.append(arr[row][endCol])
        for col in reversed(range(startCol, endCol)):
            result.append(arr[endRow][col])
        for row in reversed(range(startRow + 1, endCol)):
            result.append(arr[row][startCol])
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return result

# O(n) | O(n)


def spiralTraversal1(arr):
    result = []
    spiralFill(arr, 0, len(arr) - 1, 0, len(arr[0]) - 1, result)
    return result


def spiralFill(arr, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return
    for col in range(startCol, endCol + 1):
        result.append(arr[startRow][col])
    for row in range(startRow + 1, endRow + 1):
        result.append(arr[row][endCol])
    for col in reversed(range(startCol, endCol)):
        result.append(arr[endRow][col])
    for row in reversed(range(startRow + 1, endCol)):
        result.append(arr[row][startCol])
    spiralFill(arr, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)


print(spiralTraversal(
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
