def tree2str(root) -> str:
        res = []
        def inOrd(root):
            if not root: return
            res.append("(")
            res.append(str(root.val))
            if not root.left and root.right: res.append("()")
            inOrd(root.left)
            inOrd(root.right)
            res.append(")")
        inOrd(root)
        return "".join(res)[1:-1]
