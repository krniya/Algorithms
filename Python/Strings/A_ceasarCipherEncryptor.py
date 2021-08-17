# O(n) | O(n)
def encryptor(str, i):
    newLetter = []
    newKey = i % 26
    for letter in str:
        newLetter.append(getNewLetter(letter, newKey))
    return "".join(newLetter)


def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


# O(n) | O(n)
def encryptor2(str, i):
    newLetter = []
    newKey = i % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in str:
        newLetter.append(getNewLetter2(letter, newKey, alphabet))
    return "".join(newLetter)


def getNewLetter2(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]


print(encryptor2('niya', 32))
