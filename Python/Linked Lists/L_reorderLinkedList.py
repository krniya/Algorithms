def reorderLinkedList(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second = slow.next
    prev = slow.next = None
    while second:
        nextt = second.next
        second.next = prev
        prev = second
        second = nextt
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

def reverse(self, head):
        if not head:
            return None
        prev = None
        curr = head
        nextNode = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

def merge(self, list1, list2):
    while list2:
        nextNode = list1.next
        list1.next = list2
        list1 = list2
        list2 = nextNode

def reorderList(self, head):
    if not head or not head.next:
        return
    slow = head
    fast = head
    prev = head
    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next
    prev.next = None
    list1 = head
    list2 = self.reverse(slow)
    self.merge(list1, list2)