class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def copyRandomList(head):
        nodeToCopy = { None: None}
        curr = head
        while curr:
            copy = ListNode(curr.val)
            nodeToCopy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = nodeToCopy[curr]
            copy.next = nodeToCopy[curr.next]
            copy.random = nodeToCopy[curr.random]
            curr = curr.next
        return nodeToCopy[head]