def secFrequent(arr):
    dic = {}
    for word in arr:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    dic = sorted(dic.items(), key= lambda x:x[1])
    return dic[-2][0]
    

print(secFrequent(['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']))