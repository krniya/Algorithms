def reverseWords(s: str) -> str:
        res =[]
        s= s.split(" ")
        for word in s:
            res.append(word[::-1])
        return " ".join(res) 

print(reverseWords("Let's take LeetCode contest"))