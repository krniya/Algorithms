def reverseWords(s: str) -> str:
        res =[]
        s= s.split(" ")
        for word in s:
            res.append(word[::-1])
        return " ".join(res) 

def reverseWords(self, s: str) -> str:
        s = s.strip().split()                   #Converting s into a list to get rid of spaces
        out = []
        for word in s:                          #Reversing each word of the list using two-pointers
            i = 0
            j = (len(word) - 1)
            while (i < j):
                word = list(word)
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            a = (''.join(word))
            out.append(a)
        return(' '.join(out))


print(reverseWords("Let's take LeetCode contest"))
