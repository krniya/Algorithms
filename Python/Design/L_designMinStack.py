class MinStack:
    
    def __init__(self):
        self.minStack = []
        
    def push(self, x: int) -> None:
        minV = min(x, self.minStack[-1][-1] if self.minStack else x)
        self.minStack.append([x,minV])

    def pop(self) -> None:
        self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1][0] 

    def getMin(self) -> int:
        return self.minStack[-1][-1] 


obj = MinStack()
print(obj.push(2147483646))
print(obj.push(2147483646))
print(obj.push(2147483647))
print(obj.top())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.push(2147483647))
print(obj.top())
print(obj.getMin())
print(obj.push(-2147483648))
print(obj.top())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
