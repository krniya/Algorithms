from functools import cache


def soupServings(n: int) -> float:
        @cache()
        def dfs(a,b):
            if a<=0 and b <=0:
                return 0.5
            elif a<=0:
                return 1
            elif b<=0:
                return 0
            else:
                return 0.25 * (dfs(a-100,b)+dfs(a-75,b-25)+dfs(a-50,b-50)+dfs(a-25,b-75))
        return 1 if n > 4800 else dfs(n,n)