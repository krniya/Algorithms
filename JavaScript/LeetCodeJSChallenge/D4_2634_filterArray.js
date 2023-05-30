var filter = function (arr, fn) {
    let res = [];
    for (const i in arr) {
        if (fn(arr[i], +i)) {
            res.push(arr[i]);
        }
    }
    return res;
};
