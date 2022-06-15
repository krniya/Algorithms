def characterReplacement(s: str, k: int) -> int:
        l = 0
        res = 0
        count={}
        fmax = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            fmax = max(fmax, count[s[r]])
            while (r-l+1) - fmax >k:
                count[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res