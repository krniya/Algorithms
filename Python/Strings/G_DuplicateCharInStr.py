def duplicateCharinStr(str):
    dup = []
    count = [0] * 58
    for i in str:
        count[ord(i) - 65] += 1
    for i in range(58):
        if(count[i] > 1):
            dup.append(chr(i+65))
    print(dup)


a = "ABCDEABzzZZ"
duplicateCharinStr(a)
