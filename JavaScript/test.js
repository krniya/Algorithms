var containsDuplicate = function (nums) {
    let visited = new Set();
    for (let num of nums) {
        if (visited.has(num)) {
            return true;
        }
        visited.add(num);
    }
    return false;
};

console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));
