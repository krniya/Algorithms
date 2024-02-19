def isPowerOfTwo(n: int) -> bool:
    return n and not (n & n - 1)