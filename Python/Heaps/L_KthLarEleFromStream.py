import heapq

class KthLargest():
    
    
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

            
    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


Kthlargest = KthLargest(3, [4, 5, 8, 2])
print(Kthlargest.add(3))
print(Kthlargest.add(5))
print(Kthlargest.add(10))
print(Kthlargest.add(9))
print(Kthlargest.add(4))