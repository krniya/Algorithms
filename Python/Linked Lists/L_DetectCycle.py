def hasCycle(head) -> bool:
    seen = set()
    cur = head

    while cur:
        if cur in seen:
            return True
        seen.add(cur)
        cur = cur.next

    return False
