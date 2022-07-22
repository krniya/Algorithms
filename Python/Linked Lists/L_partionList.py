class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x: int):
        left_head = ListNode(None)  # head of the list with nodes values < x
        right_head = ListNode(None)  # head of the list with nodes values >= x
        left = left_head  # attach here nodes with values < x
        right = right_head  # attach here nodes with values >= x
        # traverse the list and attach current node to left or right nodes
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:  # head.val >= x
                right.next = head
                right = right.next
            head = head.next
        right.next = None  # set tail of the right list to None
        left.next = right_head.next  # attach left list to the right
        return left_head.next  # head of a new partitioned list