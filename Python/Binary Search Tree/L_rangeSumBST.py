def rangeSumBST(root, low: int, high: int) -> int:
        res = 0
        def preOrd(root):
            if not root:
                return
            preOrd(root.left)
            nonlocal res
            if low <= root.val <= high:
                res += root.val
            preOrd(root.right)
        preOrd(root)
        return res