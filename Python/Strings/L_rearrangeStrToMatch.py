def rearrangeCharacters(s: str, target: str) -> int:
        freqs = {} # count the letter ffrequency of string s
        for char in s:
            freqs[char] = freqs.get(char,0) + 1
            
        freqTarget = {}  # count the letter ffrequency of target s
        for c in target:
            freqTarget[c] = freqTarget.get(c,0) + 1
            
        mini = len(s) #Minimum value to be updated
        for c in target:
            mini = min(mini, freqs.get(c,0) // freqTarget[c]) # Don't forget to use freqs.get(c,0). freqs[c] can give you keyError
        return mini