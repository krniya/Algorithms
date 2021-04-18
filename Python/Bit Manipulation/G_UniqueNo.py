def singleNumber(nums):
    sol = 0
    for i in nums:
        sol ^= i
    sol &= -sol
    res = [0, 0]
    for i in nums:
        if ((i & sol) == 0):
            res[0] ^= i
        else:
            res[1] ^= i
    return res


a = [2, 3, 1, 1, 3, 4, 2, 7]
print(singleNumber(a))
