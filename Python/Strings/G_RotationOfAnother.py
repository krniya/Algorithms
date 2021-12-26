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

def rotation2(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str1
    if (temp.count(str2) > 0):
        return True
    else:
        return False

print(rotation2('abcde', 'cdeae'))


