def permuteUnique(nums):
        res = []
        nums.sort()
        def backtrack(n,cur):
            if not n:
                res.append(cur)
                return
            for i in range(len(n)):
                if i > 0 and n[i] == n[i-1]:
                    continue
                backtrack(n[:i]+n[i+1:], cur + [n[i]])
        if nums:
            backtrack(nums,[])
        return res
