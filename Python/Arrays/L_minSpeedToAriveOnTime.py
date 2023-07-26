import math

def minSpeedOnTime(dist, hour: float) -> int:
        def checkTime(speed):
            currentTime = 0
            for distance in dist[:-1]:
                time = distance / speed
                currentTime += math.ceil(time)
            currentTime += dist[-1] / speed
            return currentTime <= hour
        left, right = 1, int(1e7)
        minTime = float("inf")
        while left <= right:
            mid = (left + right) // 2
            if checkTime(mid):
                minTime = min(mid, minTime)
                right = mid - 1
            else:
                left = mid + 1
        return minTime if minTime != float("inf") else -1
    
print(minSpeedOnTime([1,1,100000],2.01))