def numberOfBeautifulIntegers(low: int, high: int, k: int) -> int:
    def eveod(num):
        e = o = 0
        while num:
            if (num % 10) % 2:
                o += 1
            else:
                e += 1
            num //=10
        return e == o
    count = 0
    while low % k:
        low+=1
    for n in range(low, high+1, k):
        if eveod(n):
            count+=1
    return count


print(numberOfBeautifulIntegers(1,10,1))