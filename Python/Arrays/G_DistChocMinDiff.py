def findMinDiff(A, M):
    mind = float("inf")
    A.sort()
    for i in range(len(A)-M +1):
        diff = A[i+M-1] - A[i]
        mind = min(mind, diff)
    return mind
        

print(findMinDiff([7, 3, 2, 4, 9, 12, 56], 3))