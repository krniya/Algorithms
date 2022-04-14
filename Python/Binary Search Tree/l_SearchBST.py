class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None