class Dequeue:
    def __init__(self) -> None:
        self.deq = []
        self.front = []

    def __len__(self):
        return len(self.deq)

    def isEmpty(self):
        return len(self.deq) == 0

    def first(self):
        if self.isEmpty():
            print("Dequeue Empty")
            return
        return self.deq[self.front]

    def addFirst(self, data):
        self.deq.insert(self.front, data)

    def addLast(self, data):
        self.deq.append(data)

    def removeFirst(self):
        if self.isEmpty():
            print("Dequeue Already Empty")
            return
        self.first += 1
        return self.deq.pop(self.front)

    def removeLast(self):
        if self.isEmpty():
            print("Dequeue Already Empty")
            return
        return self.deq.pop()
