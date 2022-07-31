def goodNodes(root) -> int:
        count = 0
        def dfs(root, maxN):
            if not root:
                return 0
            nonlocal count
            if root.val >= maxN: count+=1
            maxN = max(maxN, root.val)
            dfs(root.left, maxN)
            dfs(root.right, maxN)

        dfs(root, root.val)
        return count

def goodNodes(root) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)