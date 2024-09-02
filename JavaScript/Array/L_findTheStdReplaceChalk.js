var chalkReplacer = function (chalk, k) {
    let sum = 0;
    for (let x of chalk) sum += x;
    let rem = k % sum;
    for (let i = 0; i < chalk.length; i++) {
        rem -= chalk[i];
        if (rem < 0) return i;
    }
};
