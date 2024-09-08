def splitListToParts(head, k: int):
    total = 0
    curr = head
    while curr:
        curr = curr.next
        total += 1
    
    res = []
    split = total // k
    additional = total % k
    curr = head
    for _ in range(k):
        res.append(curr)
        curr_len = split + (1 if additional > 0 else 0)
        additional -= 1
        
        for _ in range(curr_len-1):
            if curr:
                curr = curr.next
        
        if curr:
            temp = curr.next
            curr.next = None
            curr = temp
    return res

                
