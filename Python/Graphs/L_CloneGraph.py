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