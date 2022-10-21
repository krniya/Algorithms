def containsNearbyDuplicate(nums, k: int) -> bool:
        visited = {}
        for i, num in enumerate(nums):
            if num in visited and i - visited[num] <= k:
                    return True
            visited[num] = i
        return False


def containsNearbyDuplicate(nums, k: int) -> bool:
        seen = set()
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False