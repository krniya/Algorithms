var maxProfitAssignment = function (difficulty, profit, worker) {
    let maxDifficulty = Math.max(...difficulty);
    let maxProfitUpToDifficulty = new Array(maxDifficulty + 1).fill(0);

    for (let i = 0; i < difficulty.length; i++) {
        maxProfitUpToDifficulty[difficulty[i]] = Math.max(
            maxProfitUpToDifficulty[difficulty[i]],
            profit[i]
        );
    }

    for (let i = 1; i <= maxDifficulty; i++) {
        maxProfitUpToDifficulty[i] = Math.max(
            maxProfitUpToDifficulty[i],
            maxProfitUpToDifficulty[i - 1]
        );
    }

    let totalProfit = 0;
    for (let ability of worker) {
        if (ability > maxDifficulty) {
            totalProfit += maxProfitUpToDifficulty[maxDifficulty];
        } else {
            totalProfit += maxProfitUpToDifficulty[ability];
        }
    }

    return totalProfit;
};
