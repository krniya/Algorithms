def noOf1bit(n):
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c

print(noOf1bit(11))