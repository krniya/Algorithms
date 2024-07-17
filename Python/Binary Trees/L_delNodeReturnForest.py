def delNodes(root, to_delete):
    s = set(to_delete)
    res = []
    def dfs(root, flag):
        if not root: return None
        toDelete = (root.val in s)
        root.left = dfs(root.left, toDelete)
        root.right = dfs(root.right, toDelete)
        if not toDelete and flag: res.append(root)
        return None if toDelete else root
    dfs(root, True)
    return res
    


