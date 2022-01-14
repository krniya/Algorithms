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
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):  
            if onesConnectToBorder[row][col]:
                continue
            matrix[row][col]= 0
    return matrix

def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectToBorder):
    stack = [(startRow, startCol)]
    while len(stack) > 0:
        currentPostion = stack.pop()
        currentRow, currentCol = currentPostion
        alreadyVisited = onesConnectToBorder[currentRow][currentCol]
        if alreadyVisited:
            continue
        onesConnectToBorder[currentRow][currentCol] = True
        neighbours = getNeighbour(matrix, currentRow, currentCol)
        for neighbour in neighbours:
            row, col = neighbour
            if matrix[row][col] != 1:
                continue
            stack.append(neighbour)

def getNeighbour(matrix, row, col):
    neighbours = []
    numRows = len(matrix)
    numCols = len(matrix[row])
    if row - 1 >= 0:
        neighbours.append((row - 1, col))
    if row + 1 < numRows:
        neighbours.append((row + 1, col))
    if col - 1 >= 0:
        neighbours.append((row, col - 1))
    if col + 1 < numCols:
        neighbours.append((row, col + 1))
    return neighbours
