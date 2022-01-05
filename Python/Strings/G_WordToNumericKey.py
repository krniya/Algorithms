def wordToNumericKey(words):
    key=[2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999]
    op= ""
    for let in words:
        if let == " ":
            op+="0"
        else:
            op += str(key[ord(let) - 97])
    return op

print(wordToNumericKey("red apple")) #777333027755533