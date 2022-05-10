class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
        if not head or not head.next:
            return head
        left = head
        right = getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = sortList(left)
        right = sortList(right)
        return merge(left,right)
    
def getMid(head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
def merge(list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next

n4 = ListNode(4)
n3 = ListNode(3)
n2 = ListNode(2)
n1 = ListNode(1)

n4.next = n3
n3.next = n2
n2.next = n1

d = n4

while d:
    print(d.val, end="->")
    d = d.next

d = sortList(n4)
print()

while d:
    print(d.val, end="->")
    d = d.next


