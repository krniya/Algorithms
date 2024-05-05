def deleteNode(node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
        
def deleteNode1(node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next.next:
                # Copy the value of the next node to the current node
                node.val = node.next.val
                # Move to the next node
                node = node.next
        # Copy the value of the last node to the current node
        node.val = node.next.val
        # Remove the last node by setting the next pointer to None
        node.next = None