var rangeSum = function (nums, n, left, right) {
    const MOD = 1000000007;

    // Find the maximum possible sum
    const maxSum = nums.reduce((a, b) => a + b, 0);

    // Count the frequency of each sum
    const count = new Array(maxSum + 1).fill(0);
    for (let i = 0; i < n; i++) {
        let sum = 0;
        for (let j = i; j < n; j++) {
            sum += nums[j];
            count[sum]++;
        }
    }

    // Calculate prefix sum of frequencies
    for (let i = 1; i <= maxSum; i++) {
        count[i] += count[i - 1];
    }

    let result = 0;
    let k = 1;
    for (let sum = 1; sum <= maxSum; sum++) {
        while (k <= count[sum]) {
            if (k >= left && k <= right) {
                result = (result + sum) % MOD;
            }
            k++;
        }
    }

    return result;
};
