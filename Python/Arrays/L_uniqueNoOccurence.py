def uniqueOccurrences(arr) -> bool:
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        visited = set()
        for num, count in counter.items():
            if count in visited:
                return False
            visited.add(count)
        return True