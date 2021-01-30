def searchInMatrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1
    l = len(matrix)
    while i < l and j >= 0:
        if(matrix[i][j] > target):
            j -= 1
        elif(matrix[i][j] < target):
            i += 1
        else:
            return True
    return False


print(searchInMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
