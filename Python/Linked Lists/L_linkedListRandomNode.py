import random

class LinkedListRandom:
    
    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        count = 0
        result = None
        curr = self.head

        while curr:
            count += 1
            # generate a random number between 1 and the count
            # if the random number is 1, update the result with the current node's value
            if random.randint(1, count) == 1:
                result = curr.val
            curr = curr.next

        return result