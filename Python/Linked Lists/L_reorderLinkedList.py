def reorderLinkedList(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second = slow.next
    prev = slow.next = None
    while second:
        nextt = second.next
        second.next = prev
        prev = second
        second = nextt
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
