from typing import List


class GCDTraverse:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums)
        maxElement = max(nums)
        if min(nums) == 1:
            return False
        factorArray = self.factorsCalculator(maxElement)
        
        parent = list(range(maxElement + 1))
        rank = [1] * (maxElement + 1)

        for num in nums:
            x = num
            while x > 1:
                p = factorArray[x]
                self.union(parent, rank, p, num)
                while x % p == 0:
                    x = x // p

        p = self.find(parent, nums[0])
        for num in nums[1:]:
            if self.find(parent, num) != p:
                return False

        return True

    def factorsCalculator(self, n: int) -> List[int]:
        dp = list(range(n + 2))
        for i in range(2, n + 1):
            if dp[i] == i:
                for j in range(i * 2, n + 1, i):
                    if dp[j] == j:
                        dp[j] = i
        return dp

    def find(self, parent: List[int], a: int) -> int:
        if parent[a] == a:
            return a
        parent[a] = self.find(parent, parent[a])
        return parent[a]

    def union(self, parent: List[int], rank: List[int], a: int, b: int) -> None:
        a = self.find(parent, a)
        b = self.find(parent, b)
        if a == b:
            return
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        rank[a] += rank[b]