class FreqStack:
    def __init__(self):
        self.count = {}
        self.maxCount = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        valCount = 1 + self.count.get(val, 0)
        self.count[val] = valCount
        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.count[res] -= 1
        if len(self.stacks[self.maxCount])==0:
            self.maxCount -= 1
        return res

obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
obj.pop()
obj.pop()
obj.pop()
obj.pop()