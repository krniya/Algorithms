def stair(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    return stair(n - 1) + stair(n-2)

def stair(n, memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    memo[n] =stair(n - 1) + stair(n-2)
    return memo[n]

print(stair(3))