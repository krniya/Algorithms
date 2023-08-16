from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def doubleIt(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    stack = []
    while head:
        stack.append(head)
        head = head.next
    newHead = None

    carry = 0
    while stack or carry:
        curr = stack.pop() if stack else None
        num = curr.val * 2 if curr else 0
        if carry:
            num += carry
            carry = 0
        if num > 9:
            carry = num//10
            num = num%10
        newNode = ListNode(num)
        newNode.next = newHead
        newHead = newNode
    return newHead