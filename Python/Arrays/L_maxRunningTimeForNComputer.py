from typing import List


def maxRunTime(n: int, batteries: List[int]) -> int:
        sumPower = sum(batteries)
        left, right = 1, sumPower // n
        
        def check(time) -> bool:
            total_power = sum(min(battery, time) for battery in batteries)
            return total_power >= time * n
        
        while left < right:
            time = (left + right + 1) // 2
            if check(time):
                left = time
            else:
                right = time - 1
        return left