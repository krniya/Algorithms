def earliestFullBloom(plantTime, growTime) -> int:
        acc_plant = 0   # accumulated plant time on each step
        min_time = 0
        for grow, cur_plant in reversed(sorted(zip(growTime, plantTime))):
		    # print accumulated plant time and plant/growth time for current plant
            log_str = " " * acc_plant + "." * cur_plant + "^" * grow
            acc_plant += cur_plant
            min_time = max(min_time, len(log_str))

        return min_time

def earliestFullBloom(plantTime, growTime) -> int:
    n = len(growTime)
    indices = sorted(range(n), key=lambda x: -growTime[x])
    plant_sum = mx = 0
    for i in indices:
        time = plant_sum + plantTime[i] + growTime[i]
        mx = max(mx, time)
        plant_sum += plantTime[i]
    return mx