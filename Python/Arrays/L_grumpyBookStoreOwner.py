def maxSatisfied(customers, grumpy, minutes):
    initial_satisfaction = 0
    max_extra_satisfaction = 0
    current_window_satisfaction = 0
    
    for i in range(len(customers)):
        if grumpy[i] == 0:
            initial_satisfaction += customers[i]
        elif i < minutes:
            current_window_satisfaction += customers[i]
    
    max_extra_satisfaction = current_window_satisfaction
    
    for i in range(minutes, len(customers)):
        current_window_satisfaction += customers[i] * grumpy[i]
        current_window_satisfaction -= customers[i - minutes] * grumpy[i - minutes]
        max_extra_satisfaction = max(max_extra_satisfaction, current_window_satisfaction)
    
    return initial_satisfaction + max_extra_satisfaction