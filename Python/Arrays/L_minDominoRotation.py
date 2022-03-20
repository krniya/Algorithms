def minDominoRotation(A,B):
    n = len(A)
    cntA = [0] * 7
    cntB = [0] * 7
    cntSame = [0] * 7
    for i in range(n):
        a, b = A[i], B[i]
        cntA[a] += 1
        cntB[b] += 1
        if a == b: cntSame[a] += 1
    ans = n
    for v in range(1, 7):
        if cntA[v] + cntB[v] - cntSame[v] == n:
            minSwap = min(cntA[v], cntB[v]) - cntSame[v]
            ans = min(ans, minSwap)
    return -1 if ans == n else ans

print(minDominoRotation([2,1,2,4,2,2],[5,2,6,2,3,2]))