var spiralMatrix = function (m, n, head) {
    const matrix = Array.from({ length: m }, () => Array(n).fill(-1));

    let topRow = 0,
        bottomRow = m - 1,
        leftColumn = 0,
        rightColumn = n - 1;

    while (head) {
        // Fill top row
        for (let col = leftColumn; col <= rightColumn && head; ++col) {
            matrix[topRow][col] = head.val;
            head = head.next;
        }
        topRow++;

        // Fill right column
        for (let row = topRow; row <= bottomRow && head; ++row) {
            matrix[row][rightColumn] = head.val;
            head = head.next;
        }
        rightColumn--;

        // Fill bottom row
        for (let col = rightColumn; col >= leftColumn && head; --col) {
            matrix[bottomRow][col] = head.val;
            head = head.next;
        }
        bottomRow--;

        // Fill left column
        for (let row = bottomRow; row >= topRow && head; --row) {
            matrix[row][leftColumn] = head.val;
            head = head.next;
        }
        leftColumn++;
    }

    return matrix;
};
