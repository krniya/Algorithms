def findJudge(n, trust):
    t = [0] * (n+1)
    for i,j in trust:
        t[i] -= 1
        t[j] += 1
    for i in range(1, n+1):
        if t[i] == n-1:
            return i
    return -1