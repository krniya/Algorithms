def pseudoPalindromicPaths(root) -> int:
        res = 0
        cdict = {}
        def dfs(root):
            if not root:
                return None
            cdict[root.val] = cdict.get(root.val, 0) + 1
            if not root.left and not root.right:
                chk = 0
                for n in cdict:
                    if cdict[n] % 2 == 1:
                        chk += 1
                if chk <= 1:
                    nonlocal res
                    res += 1
            dfs(root.left)
            dfs(root.right)
            cdict[root.val] -= 1
        dfs(root)
        return res
    

def pseudoPalindromicPaths1(root):
    count = 0
    stack = [(root, 0)]

    while stack:
        node, path = stack.pop()

        if node:
            path ^= 1 << node.val

            if not node.left and not node.right:
                if path & (path - 1) == 0:
                    count += 1
            else:
                stack.append((node.right, path))
                stack.append((node.left, path))

    return count

