class Stack:
    def __init__(self) -> None:
        self.stk = []
        self.len = 0

    def __len__(self):
        return self.len

    def isEmpty(self):
        return self.len == 0

    def push(self, num):
        self.stk.append(num)
        self.len += 1

    def pop(self):
        if self.isEmpty():
            print("Stack Alredy Empty")
            return
        self.len -= 1
        return self.stk.pop()
