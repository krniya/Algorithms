def rotateImage(matrix):
    l, r = 0, len(matrix) -1
    while l < r:
        for i in range(r - l):
            t, b = l, r
            tl = matrix[t+i][l]
            matrix[t+i][l] = matrix[b][l+i]
            matrix[b][l+i] = matrix[b-i][r]
            matrix[b-i][r] = matrix[t][r-i]
            matrix[t][r-i] = tl
        l+=1
        r-=1
    return matrix