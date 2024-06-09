var subarraysDivByK = function (nums, k) {
    let res = 0;
    let prefix = 0;
    let arr = new Array(k).fill(0);
    arr[0] = 1;

    for (let num of nums) {
        prefix = (prefix + (num % k) + k) % k;
        res += arr[prefix];
        arr[prefix]++;
    }
    return res;
};
