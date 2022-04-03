def findWinners(matches):    
    lost = {}
    people = set()
    for i, j in matches:
        people.add(i)
        people.add(j)
    for i in people:
        lost[i] = 0
    for i, j in matches:
        lost[j] += 1
    zero = []
    one = []
    for i in people:
        if lost[i] == 0:
            zero.append(i)
        elif lost[i] == 1:
            one.append(i)
    zero.sort()
    one.sort()
    return [zero, one]


print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))