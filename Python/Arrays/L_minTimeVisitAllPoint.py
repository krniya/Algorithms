from typing import List


def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    total_time = 0
    for i in range(len(points) - 1):
        x = abs(points[i][0] - points[i+1][0])
        y = abs(points[i][1] - points[i+1][1])
        total_time += max(x,y)
    return total_time