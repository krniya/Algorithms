def factorial(N):
    res = []
    prod = 1
    if N == 0:
        return prod
    while N > 1:
        prod *= N
        N-=1
    while prod > 0:
        res.append(prod%10)
        prod //= 10
    res.reverse()
    return res

print(factorial(5))
            