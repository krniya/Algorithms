def findCommon(A, B, C, n1,n2, n3) :
    i = 0
    j = 0
    k = 0 
    last = float("-inf")
    res = []
    while i < n1 and j < n2 and k < n3:
        if A[i] == B[j] == C[k]:
            if last != A[i]:
                res.append (A[i])
                last = A[i]
            i += 1
            j += 1
            k += 1    
        elif min (A[i], B[j], C[k]) == A[i]:
            i += 1
        elif min (A[i], B[j], C[k]) == B[j]:
            j += 1
        else:
            k += 1
    return res
 
print(findCommon([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120],6,5,8))