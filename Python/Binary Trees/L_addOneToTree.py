from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root, v: int, d: int):
        if d == 1:
            return TreeNode(v, root, None)
        
        bfs = deque([root])
        while bfs and d != 1:
            size = len(bfs)
            d -= 1
            for _ in range(size):
                curr = bfs.popleft()
                if curr.left != None:
                    bfs.append(curr.left)
                if curr.right != None:
                    bfs.append(curr.right)
                
                if d == 1: # Current level is in depth d-1 -> Add nodes with value `v`
                    curr.left = TreeNode(v, curr.left, None)
                    curr.right = TreeNode(v, None, curr.right)
        return root
    
def add(root, val, depth, curr):
    if not root:
        return None

    if curr == depth - 1:
        lTemp = root.left
        rTemp = root.right

        root.left = TreeNode(val)
        root.right = TreeNode(val)
        root.left.left = lTemp
        root.right.right = rTemp

        return root

    root.left = add(root.left, val, depth, curr + 1)
    root.right = add(root.right, val, depth, curr + 1)

    return root

def addOneRow(root, val, depth):
    if depth == 1:
        newRoot = TreeNode(val)
        newRoot.left = root
        return newRoot

    return add(root, val, depth, 1)