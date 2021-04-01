class Queue:
    def __init__(self) -> None:
        self.que = []
        self.front = 0
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def inqueue(self, data):
        self.size += 1
        self.que.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue Already Empty")
            return
        val = self.que[self.front]
        self.que[self.front] = None
        self.size -= 1
        self.front += 1
        return val

    def peek(self):
        if self.isEmpty():
            print("Queue Empty")
            return
        return self.que[-1]
