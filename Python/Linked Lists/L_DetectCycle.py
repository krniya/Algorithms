def hasCycle(head) -> bool:
    seen = set()
    cur = head

    while cur:
        if cur in seen:
            return True
        seen.add(cur)
        cur = cur.next

    return False

def hasCycle1(head) -> bool:
    if not head: return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False