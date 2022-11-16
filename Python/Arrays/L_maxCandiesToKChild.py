def maximumCandies(candies, k: int) -> int:
        left, right = 0, max(candies)
        while left < right:
            mid = (left + right + 1) // 2
            if k > sum(a // mid for a in candies):
                right = mid - 1
            else:
                left = mid
        return left