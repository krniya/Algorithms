def countInSorted(a,b,c):
    res = []
    i=j=k=0
    last=float("-inf")
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] and b[j] == c[k]:
            if a[i] != last:
                res.append(a[i])
                last = a[i]
            i+=1
            j+=1
            k+=1
        elif a[i] == min(a[i], b[j], c[k]):
            i+=1
        elif b[j] == min(a[i], b[j], c[k]):
            j+=1
        else:
            k+=1
    return res
        
print(countInSorted([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120]))