# O(d) | O(1)
def youngestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestoralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestoralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

def backtrackAncestoralTree(lowestDescendant, higherDescendant, diff):
    while diff > 0:
        lowestDescendant = lowestDescendant.ancestor
        diff -= 1
    while lowestDescendant != higherDescendant:
        lowestDescendant = lowestDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowestDescendant