def isSubset(a1, a2):
    s = set(a1)
    p = len(s)
    for i in range(len(a2)) :
        s.add(a2[i])
    if (len(s) == p) :
        return "Yes"
    return "No"


print(isSubset([11, 1, 13, 21, 3, 7], [11,3,7,1]))