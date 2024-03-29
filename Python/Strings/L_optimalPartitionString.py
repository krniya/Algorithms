def partitionString(s: str) -> int:
        idx = 0
        count = 0
        mp = {} # use a dictionary instead of a HashMap
        while idx < len(s):
            if s[idx] in mp: # if current character has already appeared in current substring
                count += 1 # increment count
                mp.clear() # clear dictionary to start a new substring
            mp[s[idx]] = True # mark current character as seen
            idx += 1 # move to next character
        return count + 1