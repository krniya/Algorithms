# Definition for a binary tree node.
class TreeNode:
    __slots__ = ['val', 'left', 'right']

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root.right
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini
            root.right = self.deleteNode(root.right, root.val)
        return root

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.val, end=" -> ")
            self.printInorder(root.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

sol = Solution()
# sol.printInorder(root)
# print()
sol.deleteNode(root, 3)
# sol.printInorder(root)
