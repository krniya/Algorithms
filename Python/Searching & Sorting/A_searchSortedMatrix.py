# O(n+m) | O(1)
def searchSortedMatrix(matrix, tar):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > tar:
            col-=1
        elif matrix[row][col] < tar:
            row+=1
        else:
            return [row,col]
    return [-1, -1]