import heapq


def kSmallestPairs(num1, num2, k: int):
        res = []
        minheap = []
        visited = set()
        heapq.heappush(minheap, (num1[0] + num2[0], 0, 0))
        visited.add((0,0))
        while k and minheap:
            _, i, j = heapq.heappop(minheap)
            res.append([num1[i], num2[j]])
            
            if i+1 < len(num1) and (i+1, j) not in visited:
                heapq.heappush(minheap, (num1[i+1] + num2[j], i+1, j))
                visited.add((i+1, j))
                
            if j+1 < len(num2) and (i, j+1) not in visited:
                heapq.heappush(minheap, (num1[i] + num2[j+1], i, j+1))
                visited.add((i,j+1))
                
            k-=1
        return res