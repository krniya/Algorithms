var checkSubarraySum = function (nums, k) {
    let sum = 0;
    const remainderMap = new Map();
    remainderMap.set(0, -1); // Initialize the map with remainder 0 at index -1.

    // Loop through the array.
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i]; // Increment the sum by the current element.

        // Calculate the remainder of the sum with respect to k.
        const remainder = sum % k;

        // Adjust remainder to be non-negative.
        const adjustedRemainder = remainder < 0 ? remainder + k : remainder;

        // If the remainder has been seen before.
        if (remainderMap.has(adjustedRemainder)) {
            // Check if the subarray length is at least 2.
            if (i - remainderMap.get(adjustedRemainder) > 1) {
                return true; // Valid subarray found.
            }
        } else {
            // Store the first occurrence of the remainder.
            remainderMap.set(adjustedRemainder, i);
        }
    }

    return false; // No valid subarray found.
};
