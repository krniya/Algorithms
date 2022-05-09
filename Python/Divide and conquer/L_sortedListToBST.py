def sortedListToBST(head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root