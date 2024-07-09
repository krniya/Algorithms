def averageWaitingTime(customers) -> float:
    total_wait = 0
    current_time = 0
    for arrival, ordt in customers:
        if current_time <= arrival:
            total_wait += ordt
            current_time = arrival + ordt
        else:
            total_wait += ordt + current_time - arrival
            current_time += ordt
    return total_wait / len(customers)