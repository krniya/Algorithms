def searchMatrix(matrix, target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bot = 0, row - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        if top > bot:
            return False
        fRow = (top + bot) // 2
        left, right = 0, col - 1
        while left <= right:
            m = (left + right) // 2
            if target > matrix[fRow][m]:
                left = m + 1
            elif target < matrix[fRow][m]:
                right = m - 1
            else:
                 return True
        return False