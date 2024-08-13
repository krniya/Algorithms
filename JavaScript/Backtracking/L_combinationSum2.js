var combinationSum2 = function (candidates, target) {
    candidates.sort((a, b) => a - b);
    let res = [];
    var backtrack = function (i, tar, curr) {
        if (tar == 0) {
            res.push(curr);
            return;
        }
        for (let j = i; j < candidates.length; j++) {
            if (j > i && candidates[j] === candidates[j - 1]) continue;
            if (candidates[j] > tar) break;
            backtrack(j + 1, tar - candidates[j], [...curr, candidates[j]]);
        }
    };
    if (candidates) backtrack(0, target, []);
    return res;
};

console.log(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8));
