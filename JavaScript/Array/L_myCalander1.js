var MyCalendar = function () {
    this.val = [];
};

/**
 * @param {number} start
 * @param {number} end
 * @return {boolean}
 */
MyCalendar.prototype.book = function (start, end) {
    let left = 0;
    let right = this.val.length - 1;

    while (left <= right) {
        let mid = Math.floor(left + (right - left) / 2);
        const [s, e] = this.val[mid];
        if (s < end && e > start) return false;

        if (start >= e) left = mid + 1;
        else right = mid - 1;
    }
    this.val.splice(left, 0, [start, end]);
    return true;
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */
