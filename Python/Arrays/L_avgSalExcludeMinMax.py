def average(salary) -> float:
    minimum, maximum, total = float("inf"), float("-inf"), 0
    for sal in salary:
        minimum, maximum = min(minimum, sal), max(maximum, sal)
        total += sal
    return (total - minimum - maximum) / (len(salary) - 2)
