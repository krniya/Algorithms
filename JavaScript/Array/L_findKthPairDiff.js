var smallestDistancePair = function (nums, k) {
    nums.sort((a, b) => a - b);
    let low = 0;
    let high = nums[nums.length - 1] - nums[0];

    while (low < high) {
        let mid = Math.floor((low + high) / 2);
        if (countPairs(nums, mid) < k) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }

    return low;
};

function countPairs(nums, distance) {
    let count = 0;
    let left = 0;
    for (let right = 1; right < nums.length; right++) {
        while (nums[right] - nums[left] > distance) {
            left++;
        }
        count += right - left;
    }
    return count;
}
