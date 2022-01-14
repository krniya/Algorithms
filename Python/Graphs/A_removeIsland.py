def removeIsland(matrix):
    onesConnectToBorder = [[False for col in matrix[0]] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowInBorder = row == 0 or row == len(matrix) - 1
            colInBorder = col == 0 or row == len(matrix[row]) - 1
            isBorder = rowInBorder or colInBorder
            if not isBorder:
                continue
            if matrix[row][col] != 1:
                continue
            findOnesConnectedToBorder(matrix, row, col, onesConnectToBorder)

def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectToBorder):
    stack = [(startRow, startCol)]
    while len(stack) > 0:
        currentPostion = stack.pop()
        currentRow, currentCol = currentPostion
        alreadyVisited = onesConnectToBorder[currentRow][currentCol]
        if alreadyVisited:
            continue
        onesConnectToBorder[currentRow][currentCol] = True
        