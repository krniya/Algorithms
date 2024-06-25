var minKBitFlips = function (nums, k) {
    const n = nums.length;
    let flipped = 0;
    let res = 0;
    const isFlipped = new Array(n).fill(0);

    for (let i = 0; i < n; ++i) {
        if (i >= k) {
            flipped ^= isFlipped[i - k];
        }
        if (flipped == nums[i]) {
            if (i + k > n) {
                return -1;
            }
            isFlipped[i] = 1;
            flipped ^= 1;
            res++;
        }
    }

    return res;
};
