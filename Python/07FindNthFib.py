# O(2 ^ n) | O(n)
def findNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return findNthFib(n - 1) + findNthFib(n - 2)

# O(n) | O(n)
def findNthFib1(n, memorize = {1: 0, 2: 1}):
    if n in memorize:
        return memorize[n]
    else:
        memorize[n] = findNthFib1(n - 1, memorize) + findNthFib1(n - 2, memorize)
        return memorize[n]

# O(n) | O(1)
def findNthFib2(n):
    lastTwo = [0, 1]
    count = 3
    while count <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        count += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

print(findNthFib1(7))
