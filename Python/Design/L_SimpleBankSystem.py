from typing import List


class Bank:
    
    def __init__(self, balance: List[int]):
        self.accBal = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.notValid(account1) or self.notValid(account2) or self.accBal[account1-1] < money:
            return False
        self.accBal[account2-1] += money
        self.accBal[account1-1] -= money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if self.notValid(account):
            return False
        self.accBal[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if self.notValid(account) or self.accBal[account-1] < money:
            return False
        self.accBal[account-1] -= money
        return True
        
    def notValid(self,account: int) -> bool:
        if account <= 0 or account > len(self.accBal):
            return True
        return False

obj = Bank([10, 100, 20, 50, 30])

param_1 = obj.withdraw(3, 10)
param_2 = obj.transfer(5, 1, 20)
param_3 = obj.deposit(5, 20)
param_4 = obj.transfer(3, 4, 15)
param_5 = obj.withdraw(10, 50)

print(param_1,param_2,param_3,param_4,param_5)
