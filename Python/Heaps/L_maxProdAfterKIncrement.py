import heapq

def maximumProduct(nums, k: int) -> int:
    heap = []
    for i in nums:
        heapq.heappush (heap,i)
    while k :
        current = heapq.heappop(heap)
        heapq.heappush(heap, current+1)
        k-=1           
    result =1
    while len(heap)>0:
        x= heapq.heappop(heap)
        result =(result*x )% (10**9+7)    
    return result

print(maximumProduct([6,3,3,2],2))