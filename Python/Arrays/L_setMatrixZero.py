def setZeroes(matrix):
    if not matrix:
        return None
    m = len(matrix)
    n = len(matrix[0])
    firstRowIsZero = False
    firstColIsZero = False
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if row == 0:
                    firstRowIsZero = True
                if col == 0:
                    firstColIsZero = True
                matrix[row][0] = matrix[0][col] = 0
    for row in range(1, m):
        for col in range(1, n):
            matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
    if firstRowIsZero:
        for col in range(n):
            matrix[0][col] = 0     
    if firstColIsZero:
        for row in range(m):
            matrix[row][0] = 0