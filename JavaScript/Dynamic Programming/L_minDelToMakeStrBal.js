var minimumDeletions = function (s) {
    var cb = 0,
        del = 0;
    for (char of s) {
        if (char === "a") del = Math.min(++del, cb);
        else cb++;
    }
    return del;
};
