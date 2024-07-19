var luckyNumbers = function (matrix) {
    let rows = matrix.length;
    let cols = matrix[0].length;

    let row_minimums = new Array(rows).fill(Infinity);
    let col_maximums = new Array(cols).fill(0);

    for (let row_ind = 0; row_ind < rows; ++row_ind) {
        for (let col_ind = 0; col_ind < cols; ++col_ind) {
            let el = matrix[row_ind][col_ind];
            row_minimums[row_ind] = Math.min(row_minimums[row_ind], el);
            col_maximums[col_ind] = Math.max(col_maximums[col_ind], el);
        }
    }

    for (let row_ind = 0; row_ind < rows; ++row_ind) {
        for (let col_ind = 0; col_ind < cols; ++col_ind) {
            let el = matrix[row_ind][col_ind];
            if (el == row_minimums[row_ind] && el == col_maximums[col_ind]) {
                return [el];
            }
        }
    }

    return [];
};
