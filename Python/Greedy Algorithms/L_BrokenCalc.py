def brokenCalc(startVal, tar):
    ans = 0
    while startVal < tar:
        ans+=1
        if tar % 2:
            tar+=1
        else:
            tar //= 2
    return ans + startVal - tar