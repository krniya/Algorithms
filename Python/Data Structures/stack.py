class Stack:
    def __init__(self) -> None:
        self.stk = []

    def __len__(self):
        return len(self.stk)

    def isEmpty(self):
        return len(self.stk) == 0

    def push(self, num):
        self.stk.append(num)

    def pop(self):
        if self.isEmpty():
            print("Stack Alredy Empty")
            return
        return self.stk.pop()

    def bottom(self):
        if self.isEmpty():
            print("Stack is Empty")
        return self.stk[-1]
