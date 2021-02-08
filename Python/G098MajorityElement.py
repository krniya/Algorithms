def findCandidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]


def isMajority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count += 1
    if count > len(A)/2:
        return True
    else:
        return False


def printMajority(A):
    # Find the candidate for Majority
    cand = findCandidate(A)
    # Print the candidate if it is Majority
    if isMajority(A, cand) == True:
        print(cand)
    else:
        print("No Majority Element")


a = [4, 4, 4, 3, 4, 5, 4, 6, 4, 5]
printMajority(a)
