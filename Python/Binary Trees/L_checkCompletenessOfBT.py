def isCompleteTree( root) -> bool:
        if not root:
            return True
        
        queue = [root]
        seen_null = False
        
        while queue:
            node = queue.pop(0)
            
            if node is None:
                seen_null = True
                continue
                
            if seen_null:
                return False
            
            queue.append(node.left)
            queue.append(node.right)
            
        return True