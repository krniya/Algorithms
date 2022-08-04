from collections import deque
import heapq


def leastInterval(tasks, n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        q = deque()
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time