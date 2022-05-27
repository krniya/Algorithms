class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k: int):
        dummy = ListNode(0,head)
        groupprev = dummy
        while True:
            kth = getKth(groupprev, k)
            if not kth:
                break
            groupnext = kth.next
            prev, curr = kth.next, groupprev.next
            while curr != groupnext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp
        return dummy.next
                
            
def getKth( curr, k):
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr