import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        q = collections.deque([root])
        res = []
        if not root:
            return res
        while q:
            lvl=[]
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                lvl.append(curr.val)
            res.append(lvl)
        return res