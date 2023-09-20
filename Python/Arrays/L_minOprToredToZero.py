def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        curr_sum, max_len = 0, 0
        start_idx = 0
        found = False
        for end_idx in range(len(nums)):
            curr_sum += nums[end_idx]
            while start_idx <= end_idx and curr_sum > target:
                curr_sum -= nums[start_idx]
                start_idx += 1
            if curr_sum == target:
                found = True
                max_len = max(max_len, end_idx - start_idx + 1)

        return len(nums) - max_len if found else -1


class Solution:
2
    def minOperations(self, nums: List[int], x: int) -> int:
3
        target = sum(nums) - x
4
        curr_sum, max_len = 0, 0
5
        start_idx = 0
6
        found = False
7
        for end_idx in range(len(nums)):
8
            curr_sum += nums[end_idx]
9
            while start_idx <= end_idx and curr_sum > target:
10
                curr_sum -= nums[start_idx]
11
                start_idx += 1
12
            if curr_sum == target:
13
                found = True
14
                max_len = max(max_len, end_idx - start_idx + 1)
15
​
16
        return len(nums) - max_len if found else -1
