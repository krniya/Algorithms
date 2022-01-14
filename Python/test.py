def addSpace(s, spaces):    
    tmp = ''
    i = 0
    for j in spaces:
        tmp+=s[i:j]+' '
        i = j
    tmp+=s[i:]
    return tmp

print(addSpace("LeetcodeHelpsMeLearn", [8,13,15]))