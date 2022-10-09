def findTarget(root, k: int) -> bool:
        visit = set()
        def dfs(node):
            if not node:
                return False
            if k - node.val in visit:
                return True
            else:
                visit.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)