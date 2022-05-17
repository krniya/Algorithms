
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: 
                return False
            if node == target: 
                return True
            left, right = dfs(node.left), dfs(node.right)
            if left or right:
                if left:
                    path.append(0)
                if right:
                    path.append(1)
            return left or right
                
        path = []
        dfs(original)
        for i in path[::-1]:
            cloned = cloned.left if i==0 else cloned.right
        return cloned