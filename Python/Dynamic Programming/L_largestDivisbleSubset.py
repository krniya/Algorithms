from typing import List


def largestDivisibleSubset(nums: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)
    groupSize = [1] * n
    prevElement = [-1] * n
    maxIndex = 0

    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if groupSize[i] < 1 + groupSize[j]:
                    groupSize[i] = 1 + groupSize[j]
                    prevElement[i] = j
        if groupSize[i] > groupSize[maxIndex]:
            maxIndex = i

    result = []
    while maxIndex != -1:
        result.insert(0, nums[maxIndex])
        maxIndex = prevElement[maxIndex]

    return result

def largestDivisibleSubset1(nums: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)
    dp = [1] * n
    max_size, max_index = 1, 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] > max_size:
                    max_size = dp[i]
                    max_index = i

    result = []
    num = nums[max_index]
    for i in range(max_index, -1, -1):
        if num % nums[i] == 0 and dp[i] == max_size:
            result.append(nums[i])
            num = nums[i]
            max_size -= 1

    return result


