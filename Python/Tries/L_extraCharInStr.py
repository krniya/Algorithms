class ExtraChar:
    def __init__(self):
        self.dp = [-1] * 51  # Initialize dp array with -1 values
        
    def minExtraChar(self, s, dictionary):
        return self.minExtraCharHelper(s, dictionary, 0)
    
    def minExtraCharHelper(self, s, dictionary, i):
        if i == len(s):
            return 0

        if self.dp[i] == -1:
            self.dp[i] = 1 + self.minExtraCharHelper(s, dictionary, i + 1)  # Initialize with one extra character.

            for w in dictionary:
                if s[i:i+len(w)] == w:
                    self.dp[i] = min(self.dp[i], self.minExtraCharHelper(s, dictionary, i + len(w)))  # Update if a word in the dictionary is found.

        return self.dp[i]