import random
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

