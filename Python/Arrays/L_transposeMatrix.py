def transpose(matrix):
        res = [[0]* len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]
        return res

print(transpose([[1,2,3],[4,5,6]]))