class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLinkedList(head):
    prev = None
    curr = head
    while (curr is not None):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head = prev


def reverseLinkedList1(head):
    if head is None or head.next is None:
        return head
    rest = reverseLinkedList1(head.next)
    head.next.next = head
    head.next = None
    return rest
