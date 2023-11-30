def minimumOneBitOperations(n: int) -> int:
    res = 0
    while n:
        res = -res - (n ^ (n - 1))
        n &= n - 1
    return abs(res)