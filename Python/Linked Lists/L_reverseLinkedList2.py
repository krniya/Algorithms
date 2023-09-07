def reverseBetween(head, left: int, right: int):
        dummy = ListNode(0)
        dummy.next = head
        cur, prev = head, dummy
        for _ in range(left - 1):
            cur = cur.next
            prev = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next
    
    
    
    
    
def reverseBetween(head, left: int, right: int):    
    temp = ListNode(-1)
    prev = temp
    temp.next = head
    
    for i in range(left - 1):
        prev = prev.next
    
    cur = prev.next
    
    for i in range(right - left):
        ptr = prev.next
        prev.next = cur.next
        cur.next = cur.next.next
        prev.next.next = ptr
    
    return temp.next