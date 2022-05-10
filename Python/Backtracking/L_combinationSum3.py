def combinationSum3( k: int, n: int):
        res = []
        def backtrack(arr,a,k,n):
            if n<0 and k<0:
                return
            if k==0 and n==0:
                res.append(a)
                return
            for i in range(len(arr)):
                backtrack(arr[i+1:],a+[arr[i]], k-1, n-arr[i])
        backtrack(list(range(1,10)),[],k,n)
        return res

print(combinationSum3(9,45))