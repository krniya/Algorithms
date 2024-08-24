def nearpalind(s):
    s = list(s)
    l,r = 0, len(s) - 1
    while l<=r:
        if s[l] < s[r]:
            s[r] = s[l]
        elif s[l] > s[r]:
            s[l] =  s[r]
        l+=1
        r-=1
    return "".join(s)


print(nearpalind("123"))
print(nearpalind("1"))
print(nearpalind("15236"))
print(nearpalind("957245"))
            