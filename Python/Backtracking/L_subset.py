def subsets(nums):
        # res = [[]]
        # for num in sorted(nums):
        #     res += [item+[num] for item in res]
        # return res
        res = []
        def backtrack(n,c):
            res.append(c)
            for i in range(len(n)):
                backtrack(n[i+1:], c+[n[i]])
                
        if nums:
            backtrack(nums,[])
        return res