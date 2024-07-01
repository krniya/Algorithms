var threeConsecutiveOdds = function (arr) {
    function is_odd(num) {
        return num % 2;
    }
    for (let i = 0; i < arr.length - 2; i++) {
        if (is_odd(arr[i]) && is_odd(arr[i + 1]) && is_odd(arr[i + 2])) return true;
    }
    return false;
};
