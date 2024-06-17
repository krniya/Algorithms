var judgeSquareSum = function (c) {
    let i = 0;
    let j = Math.ceil(Math.sqrt(c));
    while (i <= j) {
        let sum = i * i + j * j;
        if (sum < c) {
            i++;
        } else if (sum > c) {
            j--;
        } else {
            return true;
        }
    }
    return false;
};
