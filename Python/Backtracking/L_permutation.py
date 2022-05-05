def permute(nums):
        res = []
        def backtrack(n,cur):
            if not n:
                res.append(cur)
                return
            for i in range(len(n)):
                backtrack(n[:i]+n[i+1:], cur + [n[i]])
        if nums:
            backtrack(nums,[])
        return res

print(permute([1,2,3]))