def sqrRoot(n):
    r=n
    while r*r > n:
        r = (r + n//r) // 2
    return r

for i in range(1,26):
    print(sqrRoot(i))
