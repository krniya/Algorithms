from bisect import bisect_right
from collections import defaultdict
from typing import List


def fullBloomFlowers(flowers: List[List[int]], people: List[int]) -> List[int]:
        flower_count = defaultdict(int)

        for start, end in flowers:
            flower_count[start] += 1
            flower_count[end + 1] -= 1

        days = sorted(flower_count.keys())
        total_flowers = 0
        for day in days:
            total_flowers += flower_count[day]
            flower_count[day] = total_flowers

        answer = []
        for person_time in people:
            index = bisect_right(days, person_time)
            if index == 0:
                answer.append(0)
            else:
                answer.append(flower_count[days[index - 1]])

        return answer