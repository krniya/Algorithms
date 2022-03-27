def KWeakestRow(mat,k):
    res = {}
    op = []
    c = 0
    for arr in mat:
        res[c] = arr.count(1)
        c+=1
    res = sorted(res.items(), key = lambda x:x[1])
    for r in res[:k]:
        op.append(r[0])
    return op



print(KWeakestRow([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3))
