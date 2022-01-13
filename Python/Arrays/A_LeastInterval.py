import heapq
import collections

def leastInterval1(tasks, n):
    curr_time, h = 0, []
    for v in collections.Counter(tasks).values():
        heapq.heappush(h, -1*v)
    while h:
        temp = []
        for _ in range(n+1):
            curr_time += 1
            if h:
                x = heapq.heappop(h)
                if x != -1:
                    temp.append(x+1)
            if not h and not temp:
                break
        for item in temp:
            heapq.heappush(h, item)
    return curr_time

def leastInterval(tasks, n):
    freq = list(collections.Counter(tasks).values())
    maxFreq = max(freq)
    maxFreqCount = freq.count(maxFreq)        
    ans = (maxFreq - 1) * (n+1) + maxFreqCount
    return max(ans, len(tasks))

print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))