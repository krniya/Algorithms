def insertGreatestCommonDivisors(head):
        if not head or not head.next:
            return head

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        node1 = head
        while node1.next:
            node2 = node1.next
            gcd_value = gcd(node1.val, node2.val)
            gcd_node = ListNode(gcd_value)
            node1.next = gcd_node
            gcd_node.next = node2
            node1 = node2

        return head