var minBitFlips = function (start, goal) {
    // XOR to find differing bits between start and goal
    let xorResult = start ^ goal;
    let ans = 0;

    // Count the number of 1's in the XOR result
    while (xorResult > 0) {
        ans += xorResult & 1;
        xorResult >>= 1;
    }

    return ans;
};
