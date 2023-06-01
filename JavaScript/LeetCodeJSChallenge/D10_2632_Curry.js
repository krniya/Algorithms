var curry = function (fn) {
    let nums = [];
    return function curried(...args) {
        nums = [...nums, ...args];
        if (fn.length === nums.length) {
            const res = fn(...nums);
            nums = [];
            return res;
        } else {
            return curried;
        }
    };
};
