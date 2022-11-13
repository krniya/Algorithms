def reverseWords(s: str) -> str:
        s = s.split(" ")
        s = [w for w in s if w != ""]
        return " ".join(s[::-1])