from collections import defaultdict
from collections import deque

def removeStones(stones) -> int:
        graphX = defaultdict(list)
        graphY = defaultdict(list)
        for x,y in stones:
            graphX[x].append(y)
            graphY[y].append(x)
        connectedComponent = 0
        ### each stone should only be visited once.
        visited = set()
        for x,y in stones:
            ### if the current stone has not been visited, do a BFS from it.
            if (x,y) not in visited:
                q = deque([(x,y)])
                while q:
                    xo,yo = q.popleft()
                    ### check to see if the current stone has been visited, 
                    ### if not, get its neighbors
                    if (xo,yo) not in visited:
                        visited.add((xo,yo))
                        ### since we used two hash map to store the neighbors,
                        ### we need to get all the neighbors fron the current stone.
                        for neiY in graphX[xo]:
                            q.append((xo,neiY))
                        for neiX in graphY[yo]:
                            q.append((neiX,yo))
                ### we find another connected component
                connectedComponent += 1
        
        return len(stones)-connectedComponent