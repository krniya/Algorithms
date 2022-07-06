def fib(n: int) -> int:
        fib = [1,1]
        if n == 0:
            return 0
        if n <= 2:
            return fib[1]
        for i in range(3,n+1):
            nextFib = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = nextFib
        return fib[1]