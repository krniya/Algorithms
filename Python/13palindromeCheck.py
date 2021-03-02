# O(n^2) O(n)
def palindromeCheck(str):
    reversedStr = ""
    for i in reversed(range(len(str))):
        reversedStr += str[i]
    return str == reversedStr

#O(n) | O(n)


def palindromeCheck1(str):
    reversedChar = []
    for i in reversed(range(len(str))):
        reversedChar.append(str[i])
    return str == "".join(reversedChar)

# O(n) | O(n)


def palindromeCheck2(str, i=0):
    j = len(str) - 1 - i
    return True if i >= j else str[i] == str[j] and palindromeCheck2(str, i + 1)

# O(n) | O(1)


def palindromeCheck3(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if(str[left] != str[right]):
            return False
        left += 1
        right -= 1
    return True
