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



def subsets(nums):
        res = []
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            backtrack(i+1, subset)
            
        if nums:
            backtrack(0,[])
        return res