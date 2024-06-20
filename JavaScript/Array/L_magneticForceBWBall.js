var maxDistance = function (position, m) {
    position.sort((a, b) => a - b);
    let lo = 1;
    let hi = Math.floor((position[position.length - 1] - position[0]) / (m - 1));
    let ans = 1;

    while (lo <= hi) {
        let mid = lo + Math.floor((hi - lo) / 2);
        if (canWePlace(position, mid, m)) {
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }

    return ans;
};

function canWePlace(arr, dist, balls) {
    let countBalls = 1;
    let lastPlaced = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] - lastPlaced >= dist) {
            countBalls++;
            lastPlaced = arr[i];
        }
        if (countBalls >= balls) {
            return true;
        }
    }
    return false;
}
