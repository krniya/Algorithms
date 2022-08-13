from collections import deque


class Node:
    def __init__(self,val=0,neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    nodeToCopy = {}
    def clone(node):
        if node in nodeToCopy:
            return nodeToCopy[node]
        copy = Node(node.val)
        nodeToCopy[node] = copy
        for neighbor in node.neighbors:
            node.neighbors.append(clone(neighbor))
        return copy
    return clone(node) if node else None


def cloneGraph(node: 'Node') -> 'Node':
        if not node:
            return None
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]