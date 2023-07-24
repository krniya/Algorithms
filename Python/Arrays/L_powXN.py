def myPow(x: float, n: int) -> float:
        if n < 0:
            return 1.0 / pow(x, -n)
        return pow(x, n)
    
def pow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n % 2 == 0:
        return pow(x * x, n // 2)
    else:
        return x * pow(x * x, (n - 1) // 2)
    