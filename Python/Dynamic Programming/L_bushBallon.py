from functools import lru_cache


def maxCoins(nums) -> int:
        A = [1] + nums + [1]
        
        @lru_cache(None)
        def dfs(i, j):
            return max([A[i]*A[k]*A[j] + dfs(i,k) + dfs(k,j) for k in range(i+1, j)] or [0])
        
        return dfs(0, len(A) - 1)