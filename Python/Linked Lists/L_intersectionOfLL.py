class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode):
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa