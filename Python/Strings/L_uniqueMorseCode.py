def uniqueMorseRepresentations(words) -> int:
    alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    ans = []
    for word in words:
        ans.append("".join(alphabet[ord(s)-ord("a")] for s in word))
    return len(set(ans))