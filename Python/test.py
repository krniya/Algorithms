class Node:
    def __init__(self, left, right) -> None:
        self.v = 0
        self.lazy = 0
        self.left = None
        self.right = None
        self.tl = left
        self.tr= right

    def push(self):
        t = (self.tl + self.tr) // 2
        if self.left or self.right:
            self.left = Node(self.tl, t)
            self.right = Node(t+1, self.tr)
        if self.lazy:
            self.left.lazy = 1
            self.right.lazy = 1
            self.left.v = t + self.tl + 1
            self.right.v = self.tr - (t+1) + 1
            self.lazy = 0
    
    def query(self, l,r):
        if l>r or r<self.tl or l>self.tr:
            return 0
        if l <= self.tl and r>= self.tr:
            self.v = self.tr -self.tl  + 1
            self.lazy = 1
            return
        self.push()
        a = 0
        if self.right:
            a += self.right.query(l,r)
        if self.left:
            a += self.left.query(l,r)
        return a

    def update(self, l, r):
        if l>r or r < self.tl or l > self.tr:
            return
        if l<= self.tl and r >= self.tr:
            self.v = self.tr - self.tl + 1
            self.lazy = 1
            return
        self.push()
        if self.left:
            self.left.update(l,r)
        if self.right:
            self.right.update(l,r)
        self.v = 0
        if self.left:
            self.v += self.left.v
        if self.right:
            self.v += self.right.v


class CountIntervals:
    
    def __init__(self):
        self.root = Node(1,1000000000)

    def add(self, left: int, right: int) -> None:
        self.root.update(self, left, right)

    def count(self) -> int:
        return self.root.query(1,1000000000)