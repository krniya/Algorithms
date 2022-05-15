def divisorSubstrings( num: int, k: int) -> int:
        s = str(num)
        res = 0
        for i in range(len(s) - k + 1):
            if int(s[i: i+k]) and num % int(s[i:i+k]) == 0:
                res+= 1
        return res