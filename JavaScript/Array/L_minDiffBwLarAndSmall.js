var minDifference = function (nums) {
    if (nums.length <= 4) {
        return 0;
    }
    nums.sort((a, b) => a - b);
    let k = nums.length - 3;
    let ans = nums[nums.length - 1] - nums[0];
    for (let i = k - 1; i < nums.length; i++) {
        ans = Math.min(ans, nums[i] - nums[i - k + 1]);
    }
    return ans;
};
