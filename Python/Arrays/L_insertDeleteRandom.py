import random
from operator import setitem


class RandomizedSet:
    
    def __init__(self):
        self.dataMap = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.dataMap:
            return False
        self.dataMap[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dataMap:
            return False
        lastElement = self.data[-1]
        idxToRemove = self.dataMap[val]
        
        self.dataMap[lastElement] = idxToRemove
        self.data[idxToRemove] = lastElement
        self.data[-1] = val
        self.data.pop()
        self.dataMap.pop(val)
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.data)
    
    
class RandomizedSet:
    def __init__(self):
        self.a,self.d=[],{}


    def insert(self, v: int) -> bool:
        return (v in self.d)^1 and not (setitem(self.d,v,len(self.a)) or self.a.append(v))
        

    def remove(self, v: int) -> bool:
        return v in self.d and not (lambda e,i:i<len(self.a) and (setitem(self.a,i,e) or setitem(self.d,e,i)))(self.a.pop(),self.d.pop(v))
        

    def getRandom(self) -> int:
        return choice(self.a)

