HOME_TEAM_WON = 1


def tournamentWinner(competetions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}
    for idx, competetion in enumerate(competetions):
        result = results[idx]
        homeTeam, awayTeam = competetion
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        updateScore(winningTeam, 3, scores)
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam


def updateScore(team, point, scores):
    if team not in scores:
        scores[team] = point
    scores[team] += point


print(tournamentWinner(
    [["C#", "HTML"], ["HTML", "PYTHON"], ["PYTHON", "C#"]], [0, 0, 1]))
