def searchMatrix(matrix, target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j > -1:
            if target > matrix[i][j]:
                i+=1
            elif target < matrix[i][j]:
                j-=1
            else:
                return True
        return False