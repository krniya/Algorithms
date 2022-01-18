def reorganizeString(S):
    a = sorted(sorted(S), key=S.count)
    h = len(a) // 2
    a[1::2], a[::2] = a[:h], a[h:]
    return ''.join(a) * (a[-1:] != a[-2:-1])

print(reorganizeString("aaab"))