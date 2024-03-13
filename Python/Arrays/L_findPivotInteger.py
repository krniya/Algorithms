import math


def pivotInteger(n: int) -> int:
    sum = n * (n + 1) // 2
    a = math.sqrt(sum)

    if a - math.ceil(a) == 0:
        return int(a)
    else:
        return -1