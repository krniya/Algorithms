def combine(n: int, k: int):
        res = []
        def backtrack(i,arr):
            if len(arr) == k:
                res.append(arr)
                return
            for c in range(i,n+1):
                backtrack(c+1,arr+[c])
        if n:
            backtrack(1,[])
        return res

print(combine(4,2))