def containsNearbyDuplicate(nums, k: int) -> bool:
        visited = {}
        for i, num in enumerate(nums):
            if num in visited and i - visited[num] <= k:
                    return True
            visited[num] = i
        return False