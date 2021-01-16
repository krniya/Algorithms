# O(n) | O(1)
def removeNthNodeFromEnd(head, n):
    first = head
    second = head
    count = 1
    while count <= n:
        second = second.next
        count += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second != None:
        first = first.next
        second = second.next
    first.next = first.next.next
