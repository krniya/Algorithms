var map = function (arr, fn) {
    let res = [];
    for (const i in arr) {
        res.push(fn(arr[i], +i));
    }
    return res;
};
