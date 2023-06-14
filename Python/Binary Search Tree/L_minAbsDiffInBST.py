def getMinimumDifference(root) -> int:
        cur, stack, minDiff, prev = root, [], 10**5, -10**5
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            minDiff = min(minDiff, node.val - prev)
            prev = node.val
            cur = node.right
        
        return minDiff