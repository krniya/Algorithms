def partition(s: str):
        res = []
        partition = []
        def backtrack(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for r in range(i, len(s)):
                if isPal(s, i, r):
                    partition.append(s[i:r+1])
                    backtrack(r+1)
                    partition.pop()
        def isPal(s, i, j):
            a = s[i:j+1]
            return a == a[::-1]
        
        backtrack(0)
        return res