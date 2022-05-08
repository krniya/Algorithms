def averageOfSubtree(root) -> int:
        c = 0
        def helper(node):
            if not node:
                return [0,0]
            nonlocal c
            l = helper(node.left)
            r = helper(node.right)
            s = l[0]+r[0]+node.val
            n = l[1]+r[1]+1
            if(s//n == node.val):
                c+=1
            return [s,n]
        helper(root)
        return c