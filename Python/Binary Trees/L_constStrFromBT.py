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


def tree2str(root) -> str:
    def dfs(node):
        if not node.left and not node.right:
            return str(node.val)
        curr = str(node.val)
        if node.left:
            curr += '('+ dfs(node.left) +')'
        if node.right:
            curr += '()' if not node.left else ""
            curr += '('+ dfs(node.right) +')'
        return curr
    return dfs(root)