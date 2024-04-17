def smallestFromLeaf(root) -> str:
    # Helper function to perform DFS
    def dfs(node, path, smallest):
        if not node:
            return
        
        # Append current node's character to the path
        path.append(chr(node.val + ord('a')))
        
        # If it's a leaf node, reverse the path and compare
        if not node.left and not node.right:
            current_string = ''.join(path[::-1])  # reverse path to get string
            smallest[0] = min(smallest[0], current_string)
        
        # Recursively traverse left and right subtrees
        dfs(node.left, path, smallest)
        dfs(node.right, path, smallest)
        
        # Backtrack: remove the current node's character from the path
        path.pop()
    
    # Initialize smallest string as a large value
    smallest = [chr(ord('z') + 1)]  # Store smallest string found
    
    # Start DFS from the root with an empty path
    dfs(root, [], smallest)
    
    return smallest[0]