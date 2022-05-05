def combinationSum2(c, t):
        res = []
        c.sort()
        def backtrack(s,curr,t):
            if not t:
                res.append(curr)
                return
            for i in range(s,len(c)):
                if i > s and c[i] == c[i-1]:
                    continue
                if c[i] > t:
                    break
                backtrack(i+1,curr+[c[i]], t-c[i])
            
        if c:
            backtrack(0,[],t)
        return res