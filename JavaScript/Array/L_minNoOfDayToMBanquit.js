var minDays = function (bloomDay, m, k) {
    if (m * k > bloomDay.length) {
        return -1;
    }

    const canMakeBouquets = (bloomDay, m, k, day) => {
        let total = 0;
        let flowers = 0;
        for (let b of bloomDay) {
            if (b <= day) {
                flowers++;
                if (flowers == k) {
                    total++;
                    flowers = 0;
                }
            } else {
                flowers = 0;
            }
            if (total >= m) {
                return true;
            }
        }
        return false;
    };

    let low = 1,
        high = Math.max(...bloomDay);
    while (low < high) {
        let mid = Math.floor((low + high) / 2);
        if (canMakeBouquets(bloomDay, m, k, mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }

    return low;
};
