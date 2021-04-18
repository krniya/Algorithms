class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

# O(1) | O(1)
    def peek(self):
        return self.stack[len(self.stack) - 1]

# O(1) | O(1)
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

# O(1) | O(1)
    def push(self, num):
        newMinMax = {"min": num, "max": num}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], num)
            newMinMax["max"] = max(lastMinMax["max"], num)
        self.minMaxStack.append(newMinMax)
        self.stack.append(num)

# O(1) | O(1)
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

# O(1) | O(1)
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]


mmstk = MinMaxStack()
mmstk.push(3)
mmstk.push(6)
mmstk.push(4)
mmstk.push(8)
# mmstk.push(1)
print(mmstk.peek())
print(mmstk.getMax())
print(mmstk.getMin())
