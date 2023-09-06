def splitListToParts(head, k: int):
        count, curr = 0, head
        while curr:
            curr= curr.next
            count+= 1
        fix, rem = count // k, count % k
        res = []
        curr = head
        for i in range(k):
            res.append(curr)
            partition = fix
            if rem:
                partition += 1
                rem -= 1
            for j in range(partition - 1):
                curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
        return res