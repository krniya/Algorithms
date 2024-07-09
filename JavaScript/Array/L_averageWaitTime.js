var averageWaitingTime = function (customers) {
    let curr_time = 0;
    let total_wait = 0;
    for (let arrival of customers) {
        if (curr_time <= arrival[0]) {
            total_wait += arrival[1];
            curr_time = arrival[0] + arrival[1];
        } else {
            total_wait += arrival[1] + curr_time - arrival[0];
            curr_time += arrival[1];
        }
    }
    return total_wait / customers.length;
};
