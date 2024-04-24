def tribonacci(n: int) -> int:
        if not n:
            return 0
        first, second, third = 0, 1, 1
        for _ in range(n - 2):
            first, second, third = second, third, first + second + third
        return third
    
    
def tribonacci2(n: int) -> int:
        memo = {}
        
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            else:
                result = helper(n - 1) + helper(n - 2) + helper(n - 3)
                memo[n] = result
                return result
        
        return helper(n)