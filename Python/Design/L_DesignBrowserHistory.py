class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        
    def visit(self, url: str) -> None:
        self.curr += 1
        while self.curr < len(self.history):
            self.history.pop()

        self.history.append(url)
        
    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr-steps)
        return self.history[self.curr]
      
    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history)-1, self.curr+steps)
        return self.history[self.curr]
        


# * Linked List version
class ListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory1:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, None, self.curr)
        self.curr = self.curr.next
        
    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
      
    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
        
