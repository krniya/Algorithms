def singleNumber(A):
    ans = 0
    for i in range(0, 32):
        count = 0
        for a in A:
            if ((a >> i) & 1):
                count += 1
        ans |= ((count % 3) << i)
    return convert(ans)


def convert(x):
    if x >= 2**31:
        x -= 2**32
    return x


a = [3, 2, 7, 4, 1, 2, 4, 11]
print(singleNumber(a))
