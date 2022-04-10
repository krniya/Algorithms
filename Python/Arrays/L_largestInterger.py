def largestInterger(num):
    num = [int(i) for i in str(num)]
    odd, even = [],[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    res = 0
    even.sort()
    odd.sort()
    for i in num:
        if i%2:
            res = res*10 + odd.pop()
        else:
            res = res*10 + even.pop()
    return res


print(largestInterger(1234))

            
