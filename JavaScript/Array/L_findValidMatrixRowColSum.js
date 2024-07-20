var restoreMatrix = function (rowSum, colSum) {
    let rows = rowSum.length;
    let cols = colSum.length;
    let cur_row = 0,
        cur_col = 0;
    let res = Array.from({ length: rows }, () => Array(cols).fill(0));

    while (cur_row < rows || cur_col < cols) {
        if (cur_row >= rows) {
            res[rows - 1][cur_col] = colSum[cur_col];
            cur_col++;
            continue;
        } else if (cur_col >= cols) {
            res[cur_row][cols - 1] = rowSum[cur_row];
            cur_row++;
            continue;
        }

        let value_to_put = Math.min(rowSum[cur_row], colSum[cur_col]);
        rowSum[cur_row] -= value_to_put;
        colSum[cur_col] -= value_to_put;
        res[cur_row][cur_col] = value_to_put;

        // I write this as this because it's possible that rowSum[cur_row] == colSum[cur_col] and we'll want to move both row and col pointers
        if (rowSum[cur_row] === 0) {
            cur_row++;
        }
        if (colSum[cur_col] === 0) {
            cur_col++;
        }
    }
    return res;
};
