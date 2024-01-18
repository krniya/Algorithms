def climbStairs(n: int) -> int:
    cache = {}
    def backtrack(n):
        if n in cache:
            return cache[n]
        if n < 2:
            return 1
        cache[n] = backtrack(n-1) + backtrack(n-2)
        return cache[n]
    return backtrack(n)


def climbStairs1(n: int) -> int:
    arr=[1,1]
    if n <2:
        return arr[n]
    for i in range(2,n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]