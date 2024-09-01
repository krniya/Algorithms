var construct2DArray = function (original, m, n) {
    let result = new Array(m).fill().map(() => []);
    switch (m * n === original.length ? 1 : 0) {
        case 1:
            let i = 0;
            while (i < m) {
                result[i] = original.slice(i * n, i * n + n);
                i++;
            }
            break;
        default:
            return [];
    }
    return result;
};
