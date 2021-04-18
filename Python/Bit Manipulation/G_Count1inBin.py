def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        print(n & 1)
        n >>= 1
    return count


print(countSetBits(10))
