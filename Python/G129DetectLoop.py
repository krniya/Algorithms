def detectLoop(head):
    hare = turt = head
    while turt and turt.next:
        hare = hare.next
        turt = turt.next.next
        if hare == turt:
            return True
    return False
