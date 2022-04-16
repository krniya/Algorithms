from typing import List


class ATM:
    
    def __init__(self):
        self.cc = [0,0,0,0,0]

    def deposit(self, bc: List[int]) -> None:
        for i in range(5):
            self.cc[i]+=bc[i]

    def withdraw(self, amt: int) -> List[int]:
        if amt%10:
            return [-1]
        curr = []
        for n in self.cc:
            curr.append(n)
        ans = [0,0,0,0,0]
        def reset():
            self.cc = curr
        if self.cc[4] and amt >= 500:
            n = amt//500
            amt %= 500
            ans[4] = n
            if self.cc[4] >= n:
                self.cc[4] -= n
            else:
                reset()
                return [-1]
        if self.cc[3] and amt >= 200:
            n = amt//200
            amt %= 200
            ans[3] = n
            if self.cc[3] >= n:
                self.cc[3] -= n
            else:
                reset()
                return [-1]
        if self.cc[2] and amt >= 100:
            n = amt//100
            amt %= 100
            ans[2] = n
            if self.cc[2] >= n:
                self.cc[2] -= n
            else:
                reset()
                return [-1]
        if self.cc[1] and amt >= 50:
            n = amt//50
            amt %= 50
            ans[1] = n
            if self.cc[1] >= n:
                self.cc[1] -= n
            else:
                reset()
                return [-1]
        if self.cc[0] and amt >= 20:
            n = amt//20
            amt %= 20
            ans[0] = n
            if self.cc[0] >= n:
                self.cc[0] -= n
            else:
                reset()
                return [-1]
        if amt == 0:
            return ans
        else: 
            reset()
            return [-1]

obj = ATM()
obj.deposit([0,0,1,2,1])
print(obj.withdraw(600))
obj.deposit([0,1,0,1,1])
print(obj.withdraw(600))
print(obj.withdraw(550))
