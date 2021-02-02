def removeLoop(head):
    if head is None:
        return

    fast = head.next
    slow = head

    while fast != slow:
        if fast is None or fast.next is None:
            return
        fast = fast.next.next
        slow = slow.next

    size = 1
    fast = fast.next
    while fast != slow:
        size += 1
        fast = fast.next

    slow = head
    fast = head
    for _ in range(size-1):
        fast = fast.next

    while fast.next != slow:
        fast = fast.next
        slow = slow.next

    fast.next = None


def removeLoop2(head):
    # code here
    # remove the loop without losing any nodes
    hare = turt = head
    while hare and turt and hare.next:
        turt = turt.next
        hare = hare.next.next
        if turt == head:
            rmloop(turt, head)
            return 1
    return 0


def rmloop(loop, head):
    ptr1 = ptr2 = loop
    s = 1
    while ptr1.next != ptr2:
        s += 1
        ptr1 = ptr1.next
    ptr1 = head
    for i in range(s):
        ptr2 = ptr2.next
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    while ptr2.next != ptr1:
        ptr2 = ptr2.next
    ptr2.next = None
