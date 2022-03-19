def restoreMatrix(rowSum, colSum):
    # result = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
    result = [[0] * len(colSum) for _ in range(len(rowSum))]
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = min(rowSum[i],colSum[j])
            rowSum[i] -= result[i][j]
            colSum[j] -= result[i][j]
    return result

print(restoreMatrix([14,9],[6,9,8]))
