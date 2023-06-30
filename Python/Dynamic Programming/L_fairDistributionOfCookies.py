def distributeCookies(cookies, k: int) -> int:
        min_unfairness = float("inf")
        distribution = [0] * k
        def backtrack(i):
            nonlocal min_unfairness, distribution
            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(distribution))
                return
            if min_unfairness <= max(distribution):
                return
            for kid in range(k):
                distribution[kid] += cookies[i]
                backtrack(i + 1)
                distribution[kid] -= cookies[i]
        backtrack(0)
        return min_unfairness