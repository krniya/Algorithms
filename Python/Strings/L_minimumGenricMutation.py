from collections import deque


def minMutation(start: str, end: str, bank) -> int:
        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        
        q = deque([start])
        visited = {start}
        ### use extra variable to store mutations
        mutations = 0
        while q:
            ### use for loop to check all nodes in the q
            ### so that after the for loop, we can increment mutations by 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == end:
                    return mutations
                for nei in bank:
                    if checkNeighbor(cur,nei) and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            ### increment mutations by 1
            mutations += 1
        return -1