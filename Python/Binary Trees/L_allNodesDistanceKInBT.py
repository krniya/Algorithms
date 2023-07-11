from collections import deque
from enum import CONTINUOUS
from locale import currency

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(root: TreeNode, target: TreeNode, k: int):
    """
    The function `distanceK` takes in a binary tree `root`, a target node `target`, and an integer `k`,
    and returns a list of node values that are at a distance `k` from the target node in the binary
    tree.
    
    :param root: The root node of the binary tree
    :type root: TreeNode
    :param target: The target parameter is a TreeNode object representing the node in the binary tree
    from which we want to find the nodes at distance k
    :type target: TreeNode
    :param k: The parameter "k" represents the distance from the target node to find other nodes. It
    specifies the number of edges between the target node and the other nodes to be found
    :type k: int
    :return: a list of node values that are at a distance of `k` from the `target` node in a binary
    tree.
    """
    parents = {}
    def dfs(root):
        if not root:
            return
        if root.left:
            parents[root.left.val] = root
            dfs(root.left)
        if root.right:
            parents[root.right.val] = root
            dfs(root.right)
    dfs(root)
    queue = deque()
    queue.append(target)
    visited = set()
    visited.add(target)
    while queue and k:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current.left and current.left not in visited:
                queue.append(current.left)
                visited.add(current.left)
            if current.right and current.right not in visited:
                queue.append(current.right)
                visited.add(current.right)
            if current.val in parents and parents[current.val] not in visited:
                queue.append(parents[current.val])
                visited.add(parents[current.val])
        k-=1
    ans = []
    while queue:
        ans.append(queue.popleft().val)
    return ans
    
curr = TreeNode(3)
dumm = curr
curr.left = TreeNode(5)
target = curr.left
curr.right=  TreeNode(1)
curr = curr.left
curr.left = TreeNode(6)
curr.right = TreeNode(2)
curr = curr.right
curr.left = TreeNode(7)
curr.right = TreeNode(4)

print(distanceK(dumm, target, 2))