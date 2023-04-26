def addDigits(num: int) -> int:
    while num >= 10:
        curr = 0
        while num:
            curr += num % 10
            num //= 10
        num = curr
    return num


def addDigits(num: int) -> int:
    return 0 if num == 0 else 1 + (num - 1) % 9
