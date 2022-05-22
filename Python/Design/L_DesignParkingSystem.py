class ParkingSystem:
    
    def __init__(self, big: int, medium: int, small: int):
        self.carSlot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if(self.carSlot[carType-1]):
            self.carSlot[carType-1]-=1
            return True
        return False