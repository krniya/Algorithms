def rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    i = j = 0
    while str1[i] != str2[j]:
        j += 1
        if j == len(str2):
            return False
    for _ in range(len(str1)-1):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            return False
        if j == len(str2):
            j = 0
    return True


def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
    if size1 != size2:
        return 0
    temp = string1 + string1
    if (temp.count(string2) > 0):
        return 1
    else:
        return 0
string1 = "AACD"
string2 = "ACDA"

print(areRotations(string1, string2))

