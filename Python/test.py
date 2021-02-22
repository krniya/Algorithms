def setBits(n):
    a = int(bin(n).replace('0b', ''))
    count = 0
    while a > 0:
        if a % 10 == 1:
            count += 1
        a //= 10
    return count


print(setBits(6))
