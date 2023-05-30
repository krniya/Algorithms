var reduce = function (nums, fn, init) {
    let res = init;
    for (let num of nums) {
        res = fn(res, num);
    }
    return res;
};
