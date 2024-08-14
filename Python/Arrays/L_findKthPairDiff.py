
def smallestDistancePair(nums, k: int) -> int:
    def countPairs(distance: int) -> int:
        count = left = 0
        for right in range(1, len(nums)):
            while nums[right] - nums[left] > distance:
                left += 1
            count += right - left
        return count

    nums.sort()
    low, high = 0, nums[-1] - nums[0]
    
    while low < high:
        mid = (low + high) // 2
        if countPairs(mid) < k:
            low = mid + 1
        else:
            high = mid
    return low


print(smallestDistancePair([1,6,1], 3))