def deleteMiddle(head):
        if not head.next:
            return None
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head