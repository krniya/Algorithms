def rightSideView(root):
        res = []
        def traverse(node, depth):
            if not node:
                return None
            if len(res) <= depth:
                res.append(node.val)
            traverse(node.right, depth + 1)
            traverse(node.left,  depth + 1)
        
        traverse(root, 0)
        return res


def rightSideView(root):
        res = []
        def dfs(root, curr):
            if not root: return
            if curr == len(res):
                res.append(root.val)
            dfs(root.right, curr + 1)
            dfs(root.left, curr + 1)
        dfs(root, 0)
        return res