def countRoutes(locations, start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 1000000007
        cache = {}
        def dfs(currCity, remainingFuel):
            if remainingFuel < 0:
                return 0
            if (currCity, remainingFuel) in cache:
                return cache[(currCity, remainingFuel)]
            total = 1 if currCity == finish else 0
            for nextCity in range(n):
                if nextCity != currCity and remainingFuel >= abs(locations[nextCity] - locations[currCity]):
                    total += dfs(nextCity, remainingFuel - abs(locations[nextCity] - locations[currCity]))
            cache[(currCity, remainingFuel)] = total % MOD
            return cache[(currCity, remainingFuel)]
        return dfs(start, fuel)