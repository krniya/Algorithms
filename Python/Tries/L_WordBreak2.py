from typing import List

# * DP Solution

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
            res = []

            def dfs(idx,path):
                if (len(s) == idx):
                    res.append(' '.join(path))
                    
                for i in range(idx,len(s)):   
                    tmp = s[idx:i+1]
                    if (tmp in wordDict):
                        dfs(i+1,path+[tmp])

            dfs(0,[])
            return res 
# * Trie Solution
class Solution:
    class Trie:
        def __init__(self):
            self.root = {}
            self.WORD_DELIM = '$'
            
        def addWord(self, word):
            cur = self.root
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur[self.WORD_DELIM] = word
            
        def addWords(self, words):
            for word in words:
                self.addWord(word)
                
        def getValidSentences(self, word, res = ''):            
            res = []
            def dfs(word=word, temp=[]):
                cur = self.root
                for i,char in enumerate(word):
                    if self.WORD_DELIM in cur:
                        dfs(word[i:], temp + [cur[self.WORD_DELIM]])
                    if char not in cur:
                        break
                    cur = cur[char]
                else:
                    if self.WORD_DELIM in cur:
                        res.append(' '.join(temp + [cur[self.WORD_DELIM]]))
            dfs()
            return res
                
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = self.Trie()
        trie.addWords(wordDict)
        return trie.getValidSentences(s)

sol = Solution()
print(sol.wordBreak("catsanddog",["cat","cats","and","sand","dog"]))