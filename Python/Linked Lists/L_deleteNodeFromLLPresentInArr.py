def modifiedList(self, nums, head):
    n_set = set(nums)
    while head.val in n_set:
        head = head.next

    curr = head
    while curr and curr.next:
        temp = curr
        while temp.next and temp.next.val in n_set:
            temp = temp.next
        curr.next = temp.next
        curr = temp.next

    return head
