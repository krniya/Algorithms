def findWinners(matches):    
    winner = []
    looser = [] 
    allwin = []
    oneloss =set()
    losCnt = {}
    for match in matches:
        winner.append(match[0])
        looser.append(match[1])
    allwin = list(set(winner) - set(looser))   
    for loss in looser:
        if loss in losCnt:
            losCnt[loss] += 1
        else:
            losCnt[loss] = 1
    for win in winner:
        if win in losCnt and losCnt[win] == 1:
            oneloss.add(win)
    for win in looser:
        if win in losCnt and losCnt[win] == 1:
            oneloss.add(win)
    return [allwin,list(oneloss)]


print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))