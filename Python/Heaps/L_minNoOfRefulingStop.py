import heapq


def minRefuelStops(target: int, startFuel: int, stations) -> int:
        stations.append([target, 0])    # regard target as a station
        fuel = startFuel
        cnt, prev = 0, 0
        miss = []
    
        for pos, gas in stations:
            dis, prev = pos - prev, pos    # calculate the distance between two stations
            if fuel < dis:  # we are running out of fuel
                while miss and fuel < dis:  # use Time machine to get some fuel we missed~
                    fuel += -heapq.heappop(miss)
                    cnt += 1    # cnt is how many times we travel back to get gas
                if fuel < dis: return -1    # we have used all the gas, but still cannot get to the next station
            fuel -= dis
            heapq.heappush(miss, -gas)  # we don't need the gas until we run out of all fuel
        return cnt
