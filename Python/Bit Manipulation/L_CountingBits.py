def countBits1( n: int):
    res = [0 for _ in range(n+1)]
    offset = 1
    for i in range(1,n+1):
        if 2*offset == i:
            offset *= 2
        res[i] = res[i-offset] + 1
    return res

def countBits( num: int):
    counter = [0]
    for i in range(1, num+1):
        counter.append(counter[i >> 1] + i % 2)
    return counter

print(countBits(5))