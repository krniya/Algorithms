var numberOfSubarrays = function (nums, k) {
    let n = nums.length;
    let cnt = new Array(n + 1).fill(0);
    cnt[0] = 1;
    let ans = 0,
        t = 0;
    for (let v of nums) {
        t += v & 1;
        if (t - k >= 0) {
            ans += cnt[t - k];
        }
        cnt[t]++;
    }
    return ans;
};
