class LinkedList:
    class Node:
        __slots__ = "data", "next"

        def __init__(self, data, next) -> None:
            self.data = data
            self.next = next

    def __init__(self) -> None:
        self.head = None
        # self.next = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, data):
        new = self.Node(data, None)
        if self.isEmpty():
            self.head = next
        else:
            new.next = self.head
            self.head = new
        self.size += 1

    def addLast(self, data):
        new = self.Node(data, None)
        looper = self.head
        while looper.next is not None:
            looper = looper.next
        looper.next = new
        self.size += 1

    def addAny(self, data, idx):
        new = self.Node(data, None)
        count = 0
        nodeid = self.head
        while count < idx:
            nodeid = nodeid.next
            count += 1
        new.next = nodeid.next
        nodeid.next = new
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            print("LinkedList already Empty")
        self.head.next = self.head.next.next
        self.size -= 1

    def removeLast(self):
        if self.isEmpty():
            print("LinkedList already Empty")
        looper = self.head
        while looper.next.next is not None:
            looper = looper.next
        looper.next = None
        self.size -= 1

    def removeAny(self, idx):
        if self.isEmpty():
            print("LinkedList already Empty")
        count = 0
        nodeid = self.head
        while count < idx - 1:
            nodeid = nodeid.next
            count += 1
        nodeid.next = nodeid.next.next
        self.size -= 1
