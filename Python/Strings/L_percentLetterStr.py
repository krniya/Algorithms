def percentageLetter(s: str, letter: str) -> int:
        c=0
        for ch in s:
            if ch==letter:
                c+=1
        return ((c*100)//len(s))