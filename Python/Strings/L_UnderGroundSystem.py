from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.checkInMap = {} 
        self.routeTotalTime = defaultdict(int)
        self.routeCount = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkIn = self.checkInMap.pop(id) 
        self.routeTotalTime[(checkIn[0], stationName)] += t - checkIn[1]
        self.routeCount[(checkIn[0], stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        routeName = (startStation, endStation)
        return self.routeTotalTime[routeName] / self.routeCount[routeName]