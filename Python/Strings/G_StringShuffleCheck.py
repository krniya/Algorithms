def strShuffleCheck(str1, str2, res):
    temp = str1 + str2
    temp.sort()
    res.sort()
    i = j =0
    while i < len(res) and j < len(temp):
        if temp[i] == res[i]:
            i+=1
        j+=1
    return len(res) == i