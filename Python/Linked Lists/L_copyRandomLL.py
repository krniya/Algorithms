def copyRandomList(head):
        nodeToCopy = { None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            nodeToCopy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = nodeToCopy[curr]
            copy.next = nodeToCopy[curr.next]
            copy.random = nodeToCopy[curr.random]
            curr = curr.next
        return nodeToCopy[head]