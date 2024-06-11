var relativeSortArray = function (a, b) {
    let ans = [];
    let f = [];
    for (let i = 0; i < 1001; i++) f.push(0);
    for (let i = 0; i < a.length; i++) f[a[i]]++;
    for (let i = 0; i < b.length; i++) {
        while (f[b[i]]-- > 0) {
            ans.push(b[i]);
        }
    }
    for (let i = 0; i < 1001; i++) {
        while (f[i]-- > 0) {
            ans.push(i);
        }
    }
    return ans;
};
