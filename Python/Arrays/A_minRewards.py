# O(n^2) | O(n)
def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)

# O(n) | O(n)


def minRewards1(scores):
    rewards = [1 for _ in scores]
    localMinIdxs = getLocalMinIdx(scores)
    for localMinIdx in localMinIdxs:
        expandFromLocalMinIdx(localMinIdx, scores, rewards)
    return sum(rewards)


def expandFromLocalMinIdx(localMinIdx, scores, rewards):
    leftIdx = localMinIdx - 1
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
        leftIdx -= 1
    rightIdx = localMinIdx + 1
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
        rewards[rightIdx] = rewards[rightIdx - 1] + 1


def getLocalMinIdx(arr):
    if len(arr) == 1:
        return [0]
    localMinIdxs = []
    for i in range(len(arr)):
        if i == 0 and arr[i] < arr[i + 1]:
            localMinIdxs.append(i)
        if i == len(arr) - 1 and arr[i] < arr[i - 1]:
            localMinIdxs.append(i)
        if i == 0 or i == len(arr) - 1:
            continue
        if arr[i] < arr[i + 1] and arr[i] < arr[i - 1]:
            localMinIdxs.append(i)
    return localMinIdxs

# O(n) | O(n)


def minRewards2(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i-1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)


print(minRewards2([8, 4, 2, 1, 3, 6, 7, 9, 5, 10]))
