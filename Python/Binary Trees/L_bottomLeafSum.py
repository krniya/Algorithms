def deepestLeavesSum(root) -> int:
        sums = []
        def traverse(node,i):
            if i == len(sums):
                sums.append(0)
            sums[i] += node.val
            if node.left:
                traverse(node.left, i+1)
            if node.right:
                traverse(node.right, i+1)
        
        traverse(root, 0)
        return sums[-1]
        