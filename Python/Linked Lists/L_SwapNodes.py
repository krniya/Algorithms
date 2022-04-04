# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(k - 1):
            fast = fast.next
        first = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        first.val, slow.val = slow.val, first.val
        return head