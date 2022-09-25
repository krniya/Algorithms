class Node:
    def __init__(self, val, nxt = None):
        self.val = val
        self.nxt = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        curr = Node(value)
        if self.isEmpty():
            self.head = self.tail = curr
        else:
            self.tail.nxt = curr
            self.tail = self.tail.nxt
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = self.head.nxt
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize
