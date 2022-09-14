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