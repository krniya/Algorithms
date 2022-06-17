def countSubstrings(s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += countPali(s,i,i)
            res += countPali(s,i,i+1)
        return res
            
def countPali(s,l,r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res