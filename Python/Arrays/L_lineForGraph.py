def minimumLines(sp) -> int:
        n = len(sp)
        res = n - 1
        sp.sort()
        for i in range(1, n - 1):
            a, b, c = sp[i-1], sp[i], sp[i+1]
            if (b[0] - a[0]) * (c[1] - b[1]) == (c[0] - b[0]) * (b[1] - a[1]):
                res -= 1
        return res